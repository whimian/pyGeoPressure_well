# -*- coding: utf-8 -*-
"""
A plot widget based on matplotlib

Created on Sun Jan 21 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

import random

from PyQt4.QtCore import Qt, QSize, QTimer
from PyQt4.QtGui import QWidget, QVBoxLayout, QSizePolicy

from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
from matplotlib import rcParams

rcParams['font.size'] = 9
# self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)

        self.canvas = MyCanvas()
        self.fig = self.canvas.fig
        self.axes = self.canvas.axes

        self.canvas.setFocusPolicy(Qt.StrongFocus)
        self.canvas.setFocus()

        self.mpl_toolbar = NavigationToolbar(self.canvas, self)

        self.canvas.mpl_connect('key_press_event', self.on_key_press)

        vbox = QVBoxLayout()
        vbox.addWidget(self.mpl_toolbar)
        vbox.addWidget(self.canvas)
        self.setLayout(vbox)

    def on_key_press(self, event):
        print('you pressed', event.key)
        # implement the default mpl key press events described at
        # http://matplotlib.org/users/navigation_toolbar.html#navigation-keyboard-shortcuts
        key_press_handler(event, self.canvas, self.mpl_toolbar)

    def sizeHint(self):
        return QSize(*self.canvas.get_width_height())

    def minimumSizeHint(self):
        return QSize(10, 10)


class MyCanvas(FigureCanvas):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=None)

        self.fig = Figure(dpi=100)
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()
