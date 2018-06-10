# -*- coding: utf-8 -*-
"""
Well Marker Edit Dialog

Created on Tue May 10 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QListWidgetItem, QTableWidgetItem
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_well_marker_dialog import Ui_well_marker_Dialog
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import pygeopressure as ppp


class WellMarkerDialog(QDialog, Ui_well_marker_Dialog):
    def __init__(self, well):
        super(WellMarkerDialog, self).__init__()
        self.well = well
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        # self.setWindowIcon(QIcon(':/icon/layer_icon'))
        self.populate_marker_table()

    def populate_marker_table(self):
        try:
            markers_dict = self.well.params["horizon"]
            for mark in markers_dict.keys():
                self.tableWidget.insertRow(0)
                self.tableWidget.setItem(0, 0, QTableWidgetItem(mark))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(str(markers_dict[mark])))
                self.tableWidget.setItem(0, 2, QTableWidgetItem(str(markers_dict[mark])))
            self.tableWidget.sortItems(0, Qt.AscendingOrder)
        except KeyError:
            pass
