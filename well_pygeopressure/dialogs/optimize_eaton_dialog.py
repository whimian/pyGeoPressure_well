# -*- coding: utf-8 -*-
"""
Smooth Dialog

Created on Tue May 22 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QMessageBox,
    QListWidgetItem, QTableWidgetItem, QGridLayout)
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_optimize_eaton_dialog import (
    Ui_optimize_eaton_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import numpy as np
# from scipy.optimize import curve_fit
import pygeopressure as ppp


class OptimizeEatonDialog(QDialog, Ui_optimize_eaton_Dialog):
    def __init__(self):
        super(OptimizeEatonDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.well_listWidget.itemClicked.connect(self.handleItemChecked)
        self.contour_Button.clicked.connect(self.contour_Button_on_clicked)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        set_style()
        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_listWidget()
        self.init_axes()

    def init_axes(self):
        self.ax = self.matplotlib_widget.axes

    def update_well_listWidget(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            dnames = get_data_files(CONF.well_dir)
            # self.well_listWidget.addItems(dnames)
            for name in dnames:
                new_item = QListWidgetItem(name, self.well_listWidget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def handleItemChecked(self):
        well_names = []
        for idx in range(self.well_listWidget.count()):
            item = self.well_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                well_names.append(item.text())
        # first well
        if well_names:
            vlog_list = []
            obp_log_list = []
            nct_list = []
            n_list = []
            first_well = ppp.Well(str(CONF.well_dir / ".{}".format(well_names[0])))
            for log in first_well.logs:
                if "Velocity" in log:
                    vlog_list.append(log)
                if "Overburden" in log:
                    obp_log_list.append(log)
            for key in first_well.params.keys():
                if "nct" in key:
                    nct_list.append(key)
                if "eaton" in key:
                    n_list.append(key)

            for w_name in well_names:
                well = ppp.Well(str(CONF.well_dir / ".{}".format(w_name)))
                for log in vlog_list:
                    if log not in well.logs:
                        vlog_list.remove(log)
                for log in obp_log_list:
                    if log not in well.logs:
                        obp_log_list.remove(log)
                for key in nct_list:
                    if key not in well.params.keys():
                        nct_list.remove(key)
                for key in n_list:
                    if key not in well.params.keys():
                        n_list.remove(key)

            self.velocity_comboBox.clear()
            self.velocity_comboBox.addItems(vlog_list)
            self.obp_comboBox.clear()
            self.obp_comboBox.addItems(obp_log_list)
            self.nct_comboBox.clear()
            self.nct_comboBox.addItems(nct_list)
            # self.n_comboBox.clear()
            # self.n_comboBox.addItems(n_list)

    def contour_Button_on_clicked(self):
        well_names = []
        for idx in range(self.well_listWidget.count()):
            item = self.well_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                well_names.append(item.text())
        vel_name = str(self.velocity_comboBox.currentText())
        vel = list()
        obp = list()
        pres = list()
        vn = list()
        hydro = list()
        for well_name in well_names:
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            obp_log = well.get_log(str('Overburden_Pressure'))
            vel_log = well.get_log(vel_name)
            pres_log = well.get_pressure_measured()
            # calculate normal velocity and normal stress
            vnormal = ppp.normal(np.array(vel_log.depth),
                                 well.params['nct']['a'],
                                 well.params['nct']['b'])
            hydrostatic = ppp.hydrostatic_pressure(
                np.array(obp_log.depth), kelly_bushing=well.kelly_bushing,
                depth_w=well.water_depth)
            pres_log_data = np.array(pres_log.data)
            depth = np.array(vel_log.depth)
            for dp in pres_log.depth:
                idx = np.searchsorted(depth, dp)
                vel.append(vel_log.data[idx])
                obp.append(obp_log.data[idx])
                vn.append(vnormal[idx])
                hydro.append(hydrostatic[idx])
        vel = np.array(vel)
        obp = np.array(obp)
        pres = np.array(pres_log.data)
        vn = np.array(vn)
        hydro = np.array(hydro)
    #     print(vel, obp, pres, vn, hydro)
        n_list = np.arange(float(self.min_lineEdit.text()),
                            float(self.max_lineEdit.text()),
                            0.01)
        error = np.full_like(n_list, np.nan)
        for i, n in enumerate(error):
            error[i] = rms_delta_p(vel, pres, vn, hydro, obp, n_list[i])

        self.ax.cla()
        self.ax.set_title("Eaton Exponent Optimization")
        self.ax.set_ylabel("$\Delta {P}_{rms}$(mPa)")
        self.ax.set_xlabel('n')
        error_plot = self.ax.plot(n_list, error)

        x = n_list[np.argmin(error)]
        self.n_lineEdit.setText("{}".format(x))
        self.ax.axvline(x=x, color='brown')
        ymin, ymax = self.ax.get_ylim()
        y = (ymin + ymax)/2.
        self.ax.annotate('n={}'.format(x), xy=(x, y), xytext=(x+0.5, y),
                         arrowprops=dict(facecolor='black', shrink=0.05,
                                         width=0.1, headwidth=8))
        self.matplotlib_widget.fig.canvas.draw()

    def save_Button_on_clicked(self):
        key_to_save = self.lineEdit.text()
        value_to_save = float(self.n_lineEdit.text())

def rms_delta_p(vel, pres, vn, hydrostatic, lithostatic, ne):
    predict = ppp.eaton(vel, vn, hydrostatic, lithostatic, ne)
    measure = pres
    delta = np.sqrt(np.mean((measure - predict)**2))
    denominator = np.sqrt(np.mean(measure**2))
    return delta/denominator

def set_style():
    plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
