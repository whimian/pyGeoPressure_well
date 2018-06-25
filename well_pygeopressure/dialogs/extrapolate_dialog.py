# -*- coding: utf-8 -*-
"""
Extrapolate Logs Dialog

Created on Tue May 23 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QMessageBox,
    QListWidgetItem, QTableWidgetItem, QGridLayout)
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_extrapolate_dialog import (
    Ui_extrapolate_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pygeopressure as ppp


class ExtrapolateDialog(QDialog, Ui_extrapolate_Dialog):
    def __init__(self):
        super(ExtrapolateDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.well_comboBox.currentIndexChanged.connect(
            self.update_log_comboBox)
        self.well_comboBox.currentIndexChanged.connect(
            self.update_horizon_listWidget)
        self.log_comboBox.currentIndexChanged.connect(self.plot_left_log)
        self.sm_log_comboBox.currentIndexChanged.connect(self.plot_right_log)
        # buttons
        self.plot_horizon_Button.clicked.connect(self.draw_horizon)
        self.fit_Button.clicked.connect(self.fit_button_on_clicked)
        self.clear_Button.clicked.connect(self.clear_lines)
        self.draw_Button.clicked.connect(self.draw_line_with_a_b)
        self.extrapolate_Button.clicked.connect(self.extrapolate)
        self.save_Button.clicked.connect(self.save)
        # self.P1 = []
        # self.P2 = []
        self.fit_line_ax = []
        self.fit_line_ax2 = []
        # self.init_color_dict()
        self.color_dict = CONF.color_dict
        self.horizon_line = []
        # self.connect_id = None # needed for matplotlib to connect with event
        self.extraploated_log = None

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))

        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_comboBox()
        self.init_axes()

    def update_well_comboBox(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            dnames = get_data_files(CONF.well_dir)
            self.well_comboBox.addItems(dnames)

    def update_log_comboBox(self):
        self.log_comboBox.clear()
        self.sm_log_comboBox.clear()
        well_name = self.well_comboBox.currentText()
        if well_name != "":
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            for log_name in well.logs:
                if "Density" in log_name:
                    self.log_comboBox.addItem(log_name)
                    self.sm_log_comboBox.addItem(log_name)

    def update_horizon_listWidget(self):
        self.horizon_listWidget.clear()
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        try:
            horizons = well.params['horizon'].keys()
            for name in horizons:
                new_item = QListWidgetItem(name, self.horizon_listWidget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)
        except KeyError as e:
            # print(e.message)
            pass

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

    def init_axes(self):
        self.matplotlib_widget.fig.delaxes(self.matplotlib_widget.axes)
        ax1 = self.matplotlib_widget.fig.add_subplot(121)
        self.matplotlib_widget.fig.add_subplot(122, sharey=ax1)
        self.matplotlib_widget.axes = self.matplotlib_widget.fig.axes
        self.ax = self.matplotlib_widget.axes[0]
        self.ax2 = self.matplotlib_widget.axes[1]
        self.ax.invert_yaxis()
        # self.ax.set_ylim(ymax=0)
        # self.ax.set_xlim(xmin=1)
        # self.ax2.set_ylim(ymax=0)
        # self.ax2.set_xlim(xmin=1)
        plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    def plot_left_log(self):
        # get logs
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log_name = str(self.log_comboBox.currentText())
        if log_name:
            log = well.get_log(log_name)
            # Plot ----------------------------------------------------
            self.ax.cla()
            self.ax.plot(log.data, log.depth, color='gray', zorder=1,
                         linewidth=0.5)
            self.ax.set(title=well.well_name,
                        xlabel=u"Density (g/cm3)", ylabel="Depth(MD) (m)")
            self.ax.set_ylim(ymax=0)
            self.ax.set_xlim(xmin=1)
            self.matplotlib_widget.fig.canvas.draw()

    def plot_right_log(self):
        # get logs
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log_name = str(self.sm_log_comboBox.currentText())
        if log_name:
            sm_log = well.get_log(log_name)
            # axis 2 -------------------------------------------------------
            self.ax2.cla()
            self.ax2.plot(sm_log.data, sm_log.depth, color='gray', zorder=1,
                          linewidth=0.5)
            self.ax2.set_ylim(ymax=0)
            self.ax2.set_xlim(xmin=1)
            self.ax2.set(title=well.well_name,
                         xlabel=u"Density (g/cm3)", ylabel="Depth(MD) (m)")
            self.matplotlib_widget.fig.canvas.draw()

    def fit_button_on_clicked(self):
        # get well log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))
        # get interval for fitting
        if self.start_lineEdit.text() == "":
            fit_start = log.top
            self.start_lineEdit.setText("{}".format(fit_start))
        else:
            fit_start = float(self.start_lineEdit.text())

        if self.end_lineEdit.text() == "":
            fit_stop = log.bottom
            self.end_lineEdit.setText("{}".format(fit_stop))
        else:
            fit_stop = float(self.end_lineEdit.text())
        # do fitting
        shift = well.kelly_bushing + well.water_depth

        start_idx = log.get_depth_idx(fit_start)
        stop_idx = log.get_depth_idx(fit_stop) + 1
        depth = np.array(log.depth[start_idx: stop_idx + 1]) - shift
        den = np.array(log.data[start_idx: stop_idx + 1])
        # dt = vel**(-1)
        # dt_log = np.log(dt)
        fit_mask = np.isfinite(den)
        # dt_log_finite = dt_log[mask]
        # depth_finite = depth[mask]

        popt, pcov = curve_fit(ppp.traugott, depth[fit_mask], den[fit_mask])
        a, b = popt
        self.a_lineEdit.setText("{}".format(a))
        self.b_lineEdit.setText("{}".format(b))

        # plot on graph
        shift_depth = np.array(log.depth)
        mask = shift_depth >= shift
        shift_depth = shift_depth[mask]
        new_den = np.full_like(np.array(log.data), np.nan)
        new_den[mask] = ppp.traugott(shift_depth, a, b)
        self.fit_line_ax.append(self.ax.plot(new_den, log.depth)[0])
        self.fit_line_ax2.append(self.ax2.plot(new_den, log.depth)[0])
        self.matplotlib_widget.fig.canvas.draw()

    def clear_lines(self):
        while self.fit_line_ax:
            self.fit_line_ax[-1].remove()
            del self.fit_line_ax[-1]
        while self.fit_line_ax2:
            self.fit_line_ax2[-1].remove()
            del self.fit_line_ax2[-1]

        self.matplotlib_widget.fig.canvas.draw()

    def clear_points(self):
        while self.P1:
            self.P1[-1].remove()
            del self.P1[-1]
        while self.P2:
            self.P2[-1].remove()
            del self.P2[-1]

    def draw_line_with_a_b(self):
        # get well log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))
        # get a, b
        a, b = float(self.a_lineEdit.text()), float(self.b_lineEdit.text())
        shift = well.kelly_bushing + well.water_depth
        shift_depth = np.array(log.depth)
        mask = shift_depth >= shift
        shift_depth = shift_depth[mask]
        new_den = np.full_like(np.array(log.data), np.nan)
        new_den[mask] = ppp.traugott(shift_depth, a, b)
        self.fit_line_ax.append(self.ax.plot(new_den, log.depth)[0])
        self.fit_line_ax2.append(self.ax2.plot(new_den, log.depth)[0])
        self.matplotlib_widget.fig.canvas.draw()

    def extrapolate(self):
        # get well log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))
        sm_log = well.get_log(str(self.sm_log_comboBox.currentText()))
        # get a, b
        a, b = float(self.a_lineEdit.text()), float(self.b_lineEdit.text())
        shift = well.kelly_bushing + well.water_depth
        shift_depth = np.array(log.depth)
        mask = shift_depth >= shift
        shift_depth = shift_depth[mask]
        new_den = np.full_like(np.array(log.data), np.nan)
        new_den[mask] = ppp.traugott(shift_depth, a, b)

        old_den = np.array(sm_log.data)
        old_mask = np.isfinite(old_den)
        new_den[old_mask] = old_den[old_mask]

        self.extraploated_log = ppp.Log()
        self.extraploated_log.depth = sm_log.depth
        self.extraploated_log.data = new_den
        self.extraploated_log.units = sm_log.units
        # self.fit_line_ax.append(self.ax.plot(new_den, log.depth)[0])
        self.fit_line_ax2.append(self.ax2.plot(new_den, log.depth)[0])
        self.matplotlib_widget.fig.canvas.draw()

    def save(self):
        if self.extraploated_log is not None:
            well_name = self.well_comboBox.currentText()
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            log_name = str(self.log_comboBox.currentText())
            log = well.get_log(log_name)
            try:
                well.add_log(
                    self.extraploated_log,
                    name=log_name+"_extra",
                    unit=log.units)
                well.save_well()
                QMessageBox.information(
                    self, "Message", "{}".format("Succeed!"))
            except Exception as ex:
                QMessageBox.warning(
                    self, "Message", "{}".format(ex.message))
