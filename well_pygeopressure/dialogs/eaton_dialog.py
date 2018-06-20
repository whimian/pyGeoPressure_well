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
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_eaton_dialog import (
    Ui_eaton_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pygeopressure as ppp


class EatonDialog(QDialog, Ui_eaton_Dialog):
    def __init__(self):
        super(EatonDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.well_comboBox.currentIndexChanged.connect(
            self.update_log_comboBox)
        self.well_comboBox.currentIndexChanged.connect(
            self.update_horizon_listWidget)
        # self.log_comboBox.currentIndexChanged.connect(self.draw_log)
        # buttons
        self.plot_horizon_Button.clicked.connect(self.draw_horizon)
        self.predict_Button.clicked.connect(self.predict)

        # self.init_color_dict()
        self.color_dict = CONF.color_dict
        self.horizon_line = []

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        set_style()
        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_comboBox()
        self.init_axes()

        # self.two_points_groupBox.setVisible(False)

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
                if "nct" in key:
                    self.nct_comboBox.addItem(key)
                if "eaton" in key:
                    self.n_comboBox.addItem(key)

    def update_horizon_listWidget(self):
        self.horizon_listWidget.clear()
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        try:
            horizons = well.params['horizon'].keys()
            # self.horizon_listWidget.addItems(horizons)
            for name in horizons:
                new_item = QListWidgetItem(name, self.horizon_listWidget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)
        except KeyError as e:
            print(e.message)

    def draw_horizon(self):
        for line in self.horizon_line:
            del line

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
                self.horizon_line.append(
                    self.ax2.axhline(y=well.params['horizon'][key],
                                     color=color, linewidth=0.5, zorder=0))
                if 'T' in key:
                    import matplotlib.transforms as transforms
                    trans = transforms.blended_transform_factory(
                        self.ax.transAxes, self.ax.transData)
                    self.ax.text(
                        s=key, x=0.8, y=well.params['horizon'][key],
                        color=color, transform=trans, size=9)
                    trans2 = transforms.blended_transform_factory(
                        self.ax2.transAxes, self.ax2.transData)
                    self.ax2.text(
                        s=key, x=0.8, y=well.params['horizon'][key],
                        color=color, transform=trans2, size=9)
            self.matplotlib_widget.fig.canvas.draw()

    def predict(self):
        # get log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))


        obp_log = well.get_log(str(self.obp_comboBox.currentText()))
        vel_log = well.get_log(str(self.velocity_comboBox.currentText()))
        pres_log = well.get_pressure_measured()
        nct = well.params[str(self.nct_comboBox.currentText())]
        a, b = nct['a'], nct['b']
        # calculate normal velocity and normal stress
        vnormal = ppp.normal(np.array(vel_log.depth), a, b)
        hydrostatic = ppp.hydrostatic_pressure(
            np.array(obp_log.depth), kelly_bushing=well.kelly_bushing,
            depth_w=well.water_depth, rho_f=1.01)
        pressure = ppp.eaton(
            np.array(vel_log.data), vnormal, hydrostatic,
            np.array(obp_log.data), float(self.n_lineEdit.text()))
        pp = []
        depth = np.array(vel_log.depth)
        for dp in pres_log.depth:
            idx = np.searchsorted(depth, dp)
            pp.append(pressure[idx])
        mp = np.array(pres_log.data)
        pp = np.array(pp)
        RRMSE = ppp.rmse(mp, pp)
        self.ax.cla()
        # self.ax.invert_yaxis()
        self.ax.plot(pressure, obp_log.depth, color='blue')
        self.ax.plot(obp_log.data, obp_log.depth, color='green')
        self.ax.scatter(pres_log.data, pres_log.depth, color='red')
        self.ax.plot(hydrostatic, obp_log.depth, 'g--')
        self.ax.set_title('{}'.format(obp_log.name.upper().replace('_', '-')[4:]))
        self.ax.set_ylabel("Depth(m)")
        self.ax.set_xlabel("Pressure(mPa)")
        self.ax.set_xlim(xmin=0)
        self.ax.set_ylim(ymax=0)

        self.matplotlib_widget.fig.canvas.draw()

def set_style():
    plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
