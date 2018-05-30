# -*- coding: utf-8 -*-
"""
Optimize Bowers Dialog

Created on Tue May 22 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
import random
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QMessageBox,
    QListWidgetItem, QTableWidgetItem, QGridLayout)
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_optimize_bowers_dialog import (
    Ui_optimize_bowers_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import pygeopressure as ppp


class OptimizeBowersDialog(QDialog, Ui_optimize_bowers_Dialog):
    def __init__(self):
        super(OptimizeBowersDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.well_listWidget.itemClicked.connect(self.handleItemChecked)
        self.scatter_Button.clicked.connect(self.scatter_Button_on_clicked)
        self.fit_loading_Button.clicked.connect(self.fit_loading)
        self.draw_loading_Button.clicked.connect(self.draw_loading_line)
        self.clear_loading_Button.clicked.connect(self.clear_loading_line)
        self.fit_unloading_Button.clicked.connect(self.fit_unloading)
        self.draw_unloading_Button.clicked.connect(self.draw_unloading_line)
        self.clear_unloading_Button.clicked.connect(self.clear_unloading_line)

        self.line_loading = []
        self.line_unloading = []

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        set_style()
        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_listWidget()
        self.init_axes()

    def init_axes(self):
        self.ax = self.matplotlib_widget.axes
        self.colors = list(mpl.colors.cnames.keys())

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
            # for key in first_well.params.keys():
            #     if "nct" in key:
            #         nct_list.append(key)
            #     if "eaton" in key:
            #         n_list.append(key)
            pres_list = ["DST", "MDT", "EMW", "loading", "unloading", "MP"]
            for w_name in well_names:
                well = ppp.Well(str(CONF.well_dir / ".{}".format(w_name)))
                for log in vlog_list:
                    if log not in well.logs:
                        vlog_list.remove(log)
                for log in obp_log_list:
                    if log not in well.logs:
                        obp_log_list.remove(log)
                key_to_remove = []
                for key in pres_list:
                    if key not in well.params.keys():
                        key_to_remove.append(key)
                for key in key_to_remove:
                    pres_list.remove(key)

            self.velocity_comboBox.clear()
            self.velocity_comboBox.addItems(vlog_list)
            self.obp_comboBox.clear()
            self.obp_comboBox.addItems(obp_log_list)
            # self.nct_comboBox.clear()
            # self.nct_comboBox.addItems(nct_list)
            # self.n_comboBox.clear()
            # self.n_comboBox.addItems(n_list)

            self.pres_listWidget.clear()
            for name in pres_list:
                new_item = QListWidgetItem(name, self.pres_listWidget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)
        else:
            self.pres_listWidget.clear()

    def scatter_Button_on_clicked(self):
        well_names = []
        for idx in range(self.well_listWidget.count()):
            item = self.well_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                well_names.append(str(item.text()))

        vel_name = str(self.velocity_comboBox.currentText())
        obp_name = str(self.obp_comboBox.currentText())

        pres_names = []
        for idx in range(self.pres_listWidget.count()):
            item = self.pres_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                pres_names.append(str(item.text()))

        self.ax.cla()
        for well_name in well_names:
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            obp_log = well.get_log(obp_name)
            vel_log = well.get_log(vel_name)
            co2 = random.choice(self.colors)
            for pres_name in  pres_names:
                if pres_name == "MP":
                    pres_log = well.get_pressure_normal()
                else:
                    pres_log = well._get_pressure(pres_name)
                vel = list()
                obp = list()
                pres = list()

                depth = np.array(vel_log.depth)
                for dp in pres_log.depth:
                    idx = np.searchsorted(depth, dp)
                    vel.append(vel_log.data[idx])
                    obp.append(obp_log.data[idx])
                vel, obp, pres = \
                    np.array(vel), np.array(obp), np.array(pres_log.data)
                es = obp - pres

                if pres_name == "MP":
                    self.ax.scatter(
                        es, vel, color=co2, marker='d', facecolors='none')
                elif pres_name == "loading":
                    self.ax.scatter(
                        es, vel, color=co2, marker='o', facecolors='none')
                elif pres_name == "unloading":
                    self.ax.scatter(
                        es, vel, color=co2, marker='*')

        self.ax.set_ylim(ymin=1500, ymax=6000)
        self.ax.set_xlim(xmin=0, xmax=80)
        self.ax.set(xlabel="Pressure (MPa)", ylabel="Velocity (m/s)",
                    title="Velocity Variation with Effective Stress")

        self.matplotlib_widget.fig.canvas.draw()

    def save_Button_on_clicked(self):
        key_to_save = self.lineEdit.text()
        value_to_save = float(self.n_lineEdit.text())

    def fit_loading(self):
        well_names = []
        for idx in range(self.well_listWidget.count()):
            item = self.well_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                well_names.append(str(item.text()))

        vel_name = str(self.velocity_comboBox.currentText())
        obp_name = str(self.obp_comboBox.currentText())

        vel = list()
        obp = list()
        pres = list()
        for well_name in well_names:
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            obp_log = well.get_log(obp_name)
            vel_log = well.get_log(vel_name)
            # get data

            for pres_name in ["MP", "loading"]:
                if pres_name not in well.params.keys():
                    continue
                if pres_name == "MP":
                    pres_log = well.get_pressure_normal()
                else:
                    pres_log = well._get_pressure(pres_name)
                depth = np.array(vel_log.depth)
                for dp, val in zip(pres_log.depth, pres_log.data):
                    idx = np.searchsorted(depth, dp)
                    vel.append(vel_log.data[idx])
                    obp.append(obp_log.data[idx])
                    pres.append(val)
        vel, obp, pres = \
            np.array(vel), np.array(obp), np.array(pres)
        es = obp - pres
        # fit
        popt, pcov = curve_fit(ppp.virgin_curve, es, vel)
        a, b = popt
        self.a_lineEdit.setText("{}".format(a))
        self.b_lineEdit.setText("{}".format(b))
        #     RRMSE = rrmse(vel, ppp.virgin_curve(es, a, b))
        RRMSE = ppp.rmse(vel, ppp.virgin_curve(es, a, b))
        #     print('RRMSE={}'.format())
        #     print('R-squared={}'.format())
        R_squared = r2_score(vel, ppp.virgin_curve(es, a, b))
        string_output = 'RRMSE={}\n'.format(RRMSE) + \
            "R-squared={}".format(R_squared)
        self.loading_textEdit.setText(string_output)
        self.line_loading.append(self.plot_with_a_b(a, b))

        self.matplotlib_widget.fig.canvas.draw()

    def plot_with_a_b(self, a, b):
        new_es = np.arange(0, 70, 0.001)
        new_vel = ppp.virgin_curve(new_es, a, b)
        # --------------------------------------------
        self.clear_loading_line()

        line = self.ax.plot(new_es, new_vel, color='gray', zorder=0)[0]
        return line

    def draw_loading_line(self):
        a = float(self.a_lineEdit.text())
        b = float(self.b_lineEdit.text())
        self.line_loading.append(self.plot_with_a_b(a, b))
        self.matplotlib_widget.fig.canvas.draw()

    def clear_loading_line(self):
        while self.line_loading:
            self.line_loading[-1].remove()
            del self.line_loading[-1]
        self.matplotlib_widget.fig.canvas.draw()

    def fit_unloading(self):
        well_names = []
        for idx in range(self.well_listWidget.count()):
            item = self.well_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                well_names.append(str(item.text()))

        vel_name = str(self.velocity_comboBox.currentText())
        obp_name = str(self.obp_comboBox.currentText())

        vel = list()
        obp = list()
        pres = list()
        for well_name in well_names:
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            obp_log = well.get_log(obp_name)
            vel_log = well.get_log(vel_name)
            # get data
            for pres_name in ["unloading"]:
                if pres_name not in well.params.keys():
                    continue
                if pres_name == "MP":
                    pres_log = well.get_pressure_normal()
                else:
                    pres_log = well._get_pressure(pres_name)
                depth = np.array(vel_log.depth)
                for dp, val in zip(pres_log.depth, pres_log.data):
                    idx = np.searchsorted(depth, dp)
                    vel.append(vel_log.data[idx])
                    obp.append(obp_log.data[idx])
                    pres.append(val)
        vel, obp, pres = \
            np.array(vel), np.array(obp), np.array(pres)
        es = obp - pres
        # fit
        v_max = float(self.vmax_lineEdit.text())
        A = float(self.a_lineEdit.text())
        B = float(self.b_lineEdit.text())

        sigma_max = ((v_max - 1524)/A)**(1/B)
        temp_dict = {"A": A, "B": B, "sigma_max": sigma_max}
        def unloading_curve(sigma, u):
            independent = temp_dict["sigma_max"]*(sigma/temp_dict["sigma_max"])**(1/u)
            return 1524 + temp_dict['A'] * independent**temp_dict['B']

        popt, pcov = curve_fit(unloading_curve, es, vel)
        U, = popt
        self.u_lineEdit.setText("{}".format(U))

        RRMSE = ppp.rmse(vel, ppp.unloading_curve(es, A, B, U, v_max))
        R_squared = r2_score(vel, ppp.unloading_curve(es, A, B, U, v_max))
        string_output = 'RRMSE={}\n'.format(RRMSE) + \
            "R-squared={}".format(R_squared)
        self.unloading_textEdit.setText(string_output)

        self.draw_unloading_line()

        # self.matplotlib_widget.fig.canvas.draw()

    def draw_unloading_line(self):
        A = float(self.a_lineEdit.text())
        B = float(self.b_lineEdit.text())
        v_max = float(self.vmax_lineEdit.text())
        U = float(self.u_lineEdit.text())

        new_es = np.arange(0, 70, 0.001)
        new_vel = ppp.unloading_curve(new_es, A, B, U, v_max)
        # --------------------------------------------
        self.clear_unloading_line()
        line = self.ax.plot(new_es, new_vel, color='gray', zorder=0)[0]

        self.line_unloading.append(line)
        self.matplotlib_widget.fig.canvas.draw()

    def clear_unloading_line(self):
        while self.line_unloading:
            self.line_unloading[-1].remove()
            del self.line_unloading[-1]
        self.matplotlib_widget.fig.canvas.draw()

# def rms_delta_p(vel, pres, vn, hydrostatic, lithostatic, ne):
#     predict = ppp.eaton(vel, vn, hydrostatic, lithostatic, ne)
#     measure = pres
#     delta = np.sqrt(np.mean((measure - predict)**2))
#     denominator = np.sqrt(np.mean(measure**2))
#     return delta/denominator

def set_style():
    plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
