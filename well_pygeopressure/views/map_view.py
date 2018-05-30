# -*- coding: utf-8 -*-
"""
a Seismic display widget based on mayavi

Created on Tue Jan 16 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from builtins import *

__author__ = "Yu Hao"

from PyQt4.QtGui import QGridLayout, QWidget

import pygeopressure as ppp

from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget


class MapView(QWidget):
    def __init__(self, parent=None):
        super(MapView, self).__init__()
        self.initUI()
        self.survey_setting = None

    def initUI(self):
        layout2 = QGridLayout(self)
        self.matplotlib_widget = MatplotlibWidget(self)
        layout2.addWidget(self.matplotlib_widget)

    def draw_map(self, survey_setting):
        # fig = self.matplotlib_widget.fig
        self.survey_setting = survey_setting
        self.fig = self.matplotlib_widget.fig
        self.fig.clf()
        self.ax = self.fig.add_subplot(111)

        self.survey_setting.draw_survey_line(self.ax)

        # retaining aspect ratio when resizing
        self.ax.set_aspect(aspect='equal', anchor='C', adjustable='datalim')
        self.fig.tight_layout()

    def draw_well_loc(self, x, y, well_names):
        # remove old well name tags
        if hasattr(self, "well_names_tags"):
            for tx in self.well_names_tags:
                tx.remove()
        if hasattr(self, "well_loc_scatter"):
            self.well_loc_scatter.remove()
        self.well_loc_scatter = self.ax.scatter(
            x, y, marker='o', facecolor='none', edgecolor='green')
        self.well_names_tags = []
        for i, nam in enumerate(well_names):
            self.well_names_tags.append(self.ax.text(x[i], y[i], nam, color='blue'))
        self.fig.canvas.draw()
