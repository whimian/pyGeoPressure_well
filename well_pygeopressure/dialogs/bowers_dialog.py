# -*- coding: utf-8 -*-
"""
Smooth Dialog

Created on Thu May 24 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QMessageBox,
    QListWidgetItem, QTableWidgetItem, QGridLayout)
from PyQt4.QtCore import Qt, pyqtSlot, QSize

from well_pygeopressure.ui.ui_bowers_dialog import (
    Ui_bowers_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pygeopressure as ppp


class BowersDialog(QDialog, Ui_bowers_Dialog):
    def __init__(self):
        super(BowersDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.well_comboBox.currentIndexChanged.connect(
            self.update_log_comboBox)
        self.well_comboBox.currentIndexChanged.connect(
            self.update_horizon_listWidget)
        self.well_comboBox.currentIndexChanged.connect(
            self.update_pres_listWidget)
        self.param_comboBox.currentIndexChanged.connect(self.update_parameters)
        # buttons
        self.plot_horizon_Button.clicked.connect(self.draw_horizon)
        self.predict_Button.clicked.connect(self.predict)

        self.init_color_dict()
        self.horizon_line = []

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        set_style()
        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_comboBox()
        self.init_axes()

    def init_axes(self):
        self.ax = self.matplotlib_widget.axes
        self.ax.invert_yaxis()

    def update_well_comboBox(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            dnames = get_data_files(CONF.well_dir)
            self.well_comboBox.addItems(dnames)

    def update_log_comboBox(self):
        well_name = self.well_comboBox.currentText()
        if well_name != "":
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            for log in well.logs:
                if "Velocity" in log:
                    self.velocity_comboBox.addItem(log)
                if "Overburden" in log:
                    self.obp_comboBox.addItem(log)
            for key in well.params.keys():
                if "bowers" in key:
                    self.param_comboBox.addItem(key)

    def update_parameters(self):
        param_name = str(self.param_comboBox.currentText())
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        param_dict = well.params[param_name]
        try:
            self.a_lineEdit.setText(str(param_dict["A"]))
            self.b_lineEdit.setText(str(param_dict["B"]))
            self.u_lineEdit.setText(str(param_dict["U"]))
            self.vmax_lineEdit.setText(str(param_dict["vmax"]))
            self.start_lineEdit.setText(str(param_dict["start_depth"]))
            self.end_lineEdit.setText(str(param_dict["end_depth"]))
        except KeyError:
            pass

    def update_pres_listWidget(self):
        pres_list = ["DST", "MDT", "EMW", "loading", "unloading", "MP"]
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        key_to_remove = []
        for key in pres_list:
            if key not in well.params.keys():
                key_to_remove.append(key)
        for key in key_to_remove:
            pres_list.remove(key)

        self.pres_listWidget.clear()
        for name in pres_list:
            new_item = QListWidgetItem(name, self.pres_listWidget)
            new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
            new_item.setCheckState(Qt.Unchecked)

    def update_horizon_listWidget(self):
        self.horizon_listWidget.clear()
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        horizons = well.params['horizon'].keys()
        # self.horizon_listWidget.addItems(horizons)
        for name in horizons:
            new_item = QListWidgetItem(name, self.horizon_listWidget)
            new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
            new_item.setCheckState(Qt.Unchecked)

    def draw_horizon(self):
        while self.horizon_line:
            self.horizon_line[-1].remove()
            del self.horizon_line[-1]

        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

        for idx in range(self.horizon_listWidget.count()):
            item = self.horizon_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                key = str(item.text())
                try:
                    color = self.color_dict[key]
                except KeyError:
                    color = 'black'
                self.horizon_line.append(
                    self.ax.axhline(y=well.params['horizon'][key],
                                    color=color, linewidth=0.5, zorder=0))
                if 'T' in key:
                    import matplotlib.transforms as transforms
                    trans = transforms.blended_transform_factory(
                        self.ax.transAxes, self.ax.transData)
                    self.horizon_line.append(self.ax.text(
                        s=key, x=0.8, y=well.params['horizon'][key],
                        color=color, transform=trans, size=9))
            self.matplotlib_widget.fig.canvas.draw()

    def predict(self):
        # get log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

        obp_log = well.get_log(str(self.obp_comboBox.currentText()))
        vel_log = well.get_log(str(self.velocity_comboBox.currentText()))
        A = float(self.a_lineEdit.text())
        B = float(self.b_lineEdit.text())
        U = float(self.u_lineEdit.text())
        v_max = float(self.vmax_lineEdit.text())
        idx = obp_log.get_depth_idx(float(self.start_lineEdit.text()))
        if self.buffer_checkBox.checkState() == Qt.Checked:
            pressure = ppp.bowers_varu(
                np.array(vel_log.data), np.array(obp_log.data), U, idx,
                a=A, b=B, vmax=v_max, buf=int(self.buffer_lineEdit.text()),
                end_idx=obp_log.get_depth_idx(float(self.end_lineEdit.text())))
        else:
            pressure = ppp.bowers(
                np.array(vel_log.data), np.array(obp_log.data), U, idx,
                a=A, b=B, vmax=v_max,
                end_idx=obp_log.get_depth_idx(float(self.end_lineEdit.text())))
        # pressure = ppp.bowers(
        #     average_data, np.array(obp_log.data), U, idx,
        #     a=A, b=B, vmax=v_max,
        #     end_idx=obp_log.get_depth_idx(float(self.end_lineEdit.text())))
        # pressure = ppp.bowers_varu(
        #     average_data, np.array(obp_log.data), U, idx,
        #     a=A, b=B, vmax=v_max, buf=int(self.buffer_lineEdit.text()),
        #     end_idx=obp_log.get_depth_idx(float(self.end_lineEdit.text())))
        self.plot_pressure(pressure)

    def plot_pressure(self, pressure):
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

        obp_log = well.get_log(str(self.obp_comboBox.currentText()))

        hydrostatic = ppp.hydrostatic_pressure(
            np.array(obp_log.depth), kelly_bushing=well.kelly_bushing,
            depth_w=well.water_depth, rho_f=1.01)

        self.ax.cla()

        # Plot hydrostatic
        if self.hydro_checkBox.checkState() == Qt.Checked:
            self.ax.plot(hydrostatic, obp_log.depth, 'g--')
        # Plot lithostatic
        if self.litho_checkBox.checkState() == Qt.Checked:
            self.ax.plot(obp_log.data, obp_log.depth, color='green')
        # Plot predicted pressure
        self.ax.plot(pressure, obp_log.depth, color='blue')
        # Plot meassure pressure
        pres_names = []
        for idx in range(self.pres_listWidget.count()):
            item = self.pres_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                pres_names.append(str(item.text()))
        for pres_name in pres_names:
            if pres_name == "MP":
                pres_log = well.get_pressure_normal()
            else:
                pres_log = well._get_pressure(pres_name)

            if pres_name == "MP":
                self.ax.scatter(
                    pres_log.data, pres_log.depth, color='green', marker='d',
                    facecolors='none', zorder=10)
            elif pres_name == "loading":
                self.ax.scatter(
                    pres_log.data, pres_log.depth, color='yellow', marker='o',
                    facecolors='none', zorder=10)
            elif pres_name == "unloading":
                self.ax.scatter(
                    pres_log.data, pres_log.depth, color='red', marker='*',
                    zorder=10)
            else:
                self.ax.scatter(
                    pres_log.data, pres_log.depth, color='red', marker='*',
                    zorder=10)

        self.ax.set_title(
            '{}'.format(obp_log.name.upper().replace('_', '-')[4:]))
        self.ax.set_ylabel("Depth(m)")
        self.ax.set_xlabel("Pressure(mPa)")
        self.ax.set_xlim(xmin=0)
        self.ax.set_ylim(ymax=0, ymin=obp_log.depth[-1])

        self.matplotlib_widget.fig.canvas.draw()




    def init_color_dict(self):
        self.color_dict = {
            # Seismic Horizon
            'T10': 'khaki',
            'T12': 'peru',
            'T16': 'lightgreen',
            'T20': 'green',
            'T21': 'blue',
            'T30': 'MidnightBlue',
            # Hua Gang Group
            'H1': '#eff6fc',
            'H2': '#deebf7',
            'H3': '#cde0f1',
            'H4': '#b7d4ea',
            'H5': '#9ac8e0',
            'H6': '#77b5d9',
            'H7': '#58a1cf',
            'H8': '#3d8dc4',
            'H9': '#2676b8',
            'H10': '#1460a8',
            'H11': '#084a91',
            'H12': '#083370',
            # Ping Hu Group
            'P1': '#ffeee7',
            'P2': '#fee0d2',
            'P3': '#fdc6b0',
            'P4': '#fcab8f',
            'P5': '#fc8f6f',
            'P6': '#fb7353',
            'P7': '#f6553c',
            'P8': '#ea362a',
            'P9': '#d11e1f',
            'P10': '#b71319',
            'P11': '#980c13',
            'P12': '#6d010e'
        }

def set_style():
    plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
