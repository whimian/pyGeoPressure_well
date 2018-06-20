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

from well_pygeopressure.ui.ui_smooth_dialog import (
    Ui_smooth_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pygeopressure as ppp


class SmoothDialog(QDialog, Ui_smooth_Dialog):
    def __init__(self):
        super(SmoothDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.well_comboBox.currentIndexChanged.connect(
            self.update_log_comboBox)
        self.well_comboBox.currentIndexChanged.connect(
            self.update_horizon_listWidget)
        self.log_comboBox.currentIndexChanged.connect(self.draw_log)
        # buttons
        self.plot_horizon_Button.clicked.connect(self.draw_horizon)
        self.smooth_Button.clicked.connect(self.smooth)

        # self.initUI()

        # self.P1 = []
        # self.P2 = []
        # self.norm_line_ax = []
        # self.norm_line_ax2 = []
        # self.init_color_dict()
        self.color_dict = CONF.color_dict
        self.horizon_line = []
        # self.connect_id = None # needed for matplotlib to connect with event

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))

        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_comboBox()
        self.init_axes()

        # self.two_points_groupBox.setVisible(False)

    def init_axes(self):
        # self.matplotlib_widget.fig.delaxes(self.matplotlib_widget.axes)
        # ax1 = self.matplotlib_widget.fig.add_subplot(121)
        # self.matplotlib_widget.fig.add_subplot(122, sharey=ax1)
        # self.matplotlib_widget.axes = self.matplotlib_widget.fig.axes
        # self.ax = self.matplotlib_widget.axes[0]
        # self.ax2 = self.matplotlib_widget.axes[1]
        # self.ax2.set_yticklabels([])
        self.ax = self.matplotlib_widget.axes
        self.ax.invert_yaxis()
        plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    def update_well_comboBox(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            dnames = get_data_files(CONF.well_dir)
            self.well_comboBox.addItems(dnames)

    def update_log_comboBox(self):
        well_name = self.well_comboBox.currentText()
        if well_name != "":
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            self.log_comboBox.addItems(well.logs)

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

    def draw_log(self):
        # get log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))

        depth = np.array(log.depth)
        log_data = np.array(log.data)

        # plot on ax
        self.ax.clear()
        self.ax.plot(
            log_data, depth, color='lightgray', zorder=0, linewidth=0.5)

        self.ax.set(
            title=log.name, ylabel='Depth (m)',
            xlabel="{} ({})".format(log.descr, log.units))

        self.matplotlib_widget.fig.canvas.draw()

    def smooth(self):
        # get log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))

        times = int(self.times_spinBox.value())
        window_size = int(self.window_lineEdit.text())
        to_smooth = log

        smoothed_log = None
        for _ in range(times):
            smoothed_log = ppp.smooth_log(to_smooth, window_size)
            to_smooth = smoothed_log
        self.ax.plot(
            smoothed_log.data, smoothed_log.depth, linewidth=0.5)
        self.matplotlib_widget.fig.canvas.draw()
