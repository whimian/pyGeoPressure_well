# -*- coding: utf-8 -*-
"""
Log viewer Dialog

Created on Tue May 10 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from PyQt4.QtGui import QIcon, QDialog, QGridLayout

from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
import well_pygeopressure.ui.resources_rc
import matplotlib.pyplot as plt


class WellLogViewDialog(QDialog):
    def __init__(self, well_log):
        super(WellLogViewDialog, self).__init__()
        # self.setupUi(self)
        self.resize(300, 800)
        self.well_log = well_log
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/view_icon'))
        self.setWindowTitle("Well Log Viewer")
        set_style()
        layout = QGridLayout(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout.addWidget(self.matplotlib_widget)
        self.well_log.plot(self.matplotlib_widget.axes)
        self.matplotlib_widget.axes.invert_yaxis()

def set_style():
    plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
