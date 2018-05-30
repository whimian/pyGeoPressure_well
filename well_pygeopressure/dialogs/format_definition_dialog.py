# -*- coding: utf-8 -*-
"""
Format Definition Dialog

Created on Tue May 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QListWidgetItem, QTableWidgetItem
from PyQt4.QtCore import Qt, pyqtSlot, pyqtSignal

from well_pygeopressure.ui.ui_format_definition_dialog import (
    Ui_format_definition_Dialog)
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF

import well_pygeopressure.ui.resources_rc

import pygeopressure as ppp


class FormatDefinitionDialog(QDialog, Ui_format_definition_Dialog):

    format_defined = pyqtSignal(list)

    def __init__(self):
        super(FormatDefinitionDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.definition = None
        self.buttonBox.accepted.connect(self.set_definition)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        # self.populate_marker_table()

    def set_definition(self):
        # self.definition = {}
        # self.definition["well"] = int(self.wel_name_spinBox.value())
        # self.definition["x"] = int(self.x_spinBox.value())
        # self.definition["y"] = int(self.y_spinBox.value())
        # self.definition["kb"] = int(self.kb_spinBox.value())
        # self.definition["wd"] = int(self.wd_spinBox.value())
        # self.definition["td"] = int(self.td_spinBox.value())
        self.definition = []
        self.definition.append(int(self.wel_name_spinBox.value()) - 1)
        self.definition.append(int(self.x_spinBox.value()) - 1)
        self.definition.append(int(self.y_spinBox.value()) - 1)
        self.definition.append(int(self.kb_spinBox.value()) - 1)
        self.definition.append(int(self.wd_spinBox.value()) - 1)
        self.definition.append(int(self.td_spinBox.value()) - 1)
        for i, item in enumerate(self.definition):
            if item < 0:
                self.definition[i] = None
        self.format_defined.emit(self.definition)
        self.close()
