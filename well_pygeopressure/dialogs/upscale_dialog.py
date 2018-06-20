# -*- coding: utf-8 -*-
"""
Upscale Dialog

Created on Tue May 22 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QMessageBox,
    QListWidgetItem, QTableWidgetItem, QGridLayout)
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_upscale_dialog import (
    Ui_upscale_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pygeopressure as ppp


class UpscaleDialog(QDialog, Ui_upscale_Dialog):
    def __init__(self):
        super(UpscaleDialog, self).__init__()
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
        self.upscale_Button.clicked.connect(self.upscale)
        self.save_Button.clicked.connect(self.save)

        self.init_color_dict()
        self.horizon_line = []

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))

        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_comboBox()
        self.init_axes()

    def init_axes(self):
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

    def upscale(self):
        # get log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))

        freq = int(self.freq_spinBox.value())

        upscaled_log = ppp.upscale_log(log, freq=freq)

        self.ax.plot(
            upscaled_log.data, upscaled_log.depth, linewidth=0.5)
        self.matplotlib_widget.fig.canvas.draw()

    def save(self):
        """Save upscaled log to well"""
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log_name = str(self.log_comboBox.currentText())
        log = well.get_log(log_name)

        freq = int(self.freq_spinBox.value())

        upscaled_log = ppp.upscale_log(log, freq=freq)

        well.add_log(upscaled_log, name=log_name+"_filter{}".format(freq))
        well.save_well()

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
