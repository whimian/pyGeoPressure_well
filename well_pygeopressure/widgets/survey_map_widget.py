# -*- coding: utf-8 -*-
"""
A survey map widget

Created on Sat Jan 20 2018
"""
from __future__ import division, absolute_import, unicode_literals

__author__ = "Yu Hao"

from pyface.qt.QtGui import QWidget, QPainter, QPen
from pyface.qt.QtCore import QPoint, Qt


class SurveyMap(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.inlines = None
        self.crlines = None
        self.x_canvas = None
        self.y_canvas = None

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.plot_survey(qp)
        qp.end()

    def plot_survey(self, qp):
        if self.x_canvas is not None:
            pen = QPen(Qt.blue, 1, Qt.SolidLine)
            qp.setPen(pen)
            # draw survey area rectangle
            qp.drawLine(self.x_canvas[0], self.y_canvas[0],
                        self.x_canvas[1], self.y_canvas[1])
            qp.drawLine(self.x_canvas[1], self.y_canvas[1],
                        self.x_canvas[2], self.y_canvas[2])
            qp.drawLine(self.x_canvas[2], self.y_canvas[2],
                        self.x_canvas[3], self.y_canvas[3])
            qp.drawLine(self.x_canvas[3], self.y_canvas[3],
                        self.x_canvas[0], self.y_canvas[0])
            # draw inl/crl label
            qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
            for x, y, inl, crl in zip(
                    self.x_canvas, self.y_canvas, self.inlines, self.crlines):
                qp.drawText(QPoint(x, y), "{}/{}".format(inl, crl))
