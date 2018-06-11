# -*- coding: utf-8 -*-
"""
Log Export Dialog

Created on Mon Jun 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from PyQt4.QtGui import (QIcon, QDialog, QGridLayout, QPushButton,
                         QDialogButtonBox, QMessageBox, QLabel, QLineEdit,
                         QFileDialog)
from PyQt4.QtCore import Qt, QRect, QSize
import well_pygeopressure.ui.resources_rc

from well_pygeopressure.config import CONF
import pygeopressure as ppp


class WellLogExportDialog(QDialog):
    def __init__(self, well_log):
        super(WellLogExportDialog, self).__init__()

        self.well_log = well_log

        self.resize(400, 100)
        self.initUI()
        self.button_box.accepted.connect(self.export_log)
        self.button_box.rejected.connect(self.close)
        self.select_Button.clicked.connect(self.select_file)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        self.setWindowTitle("Export '{}'".format(self.well_log.descr))
        self.layout = QGridLayout(self)
        # add QLabel
        self.label = QLabel(self)
        self.label.setGeometry(QRect(0, 24, 31, 20))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setText("Output File:")
        self.layout.addWidget(self.label, 0, 0)
        # add QLineEdit
        self.file_path_lineEdit = QLineEdit(self)
        self.file_path_lineEdit.setGeometry(QRect(50, 24, 81, 20))
        self.layout.addWidget(self.file_path_lineEdit, 0, 1)
        # add Button
        self.select_Button = QPushButton(self)
        self.select_Button.setMaximumSize(QSize(61, 24))
        self.select_Button.setText("Select")
        self.layout.addWidget(self.select_Button, 0, 2)
        # add QDialogButtonBox
        self.button_box = QDialogButtonBox(self)
        self.button_box.setStandardButtons(
            QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box, 1, 0, 1, 3)

    def export_log(self):
        file_name = self.file_path_lineEdit.text()
        self.well_log.write_od(file_name)
        self.close()

    def select_file(self):
        fl = QFileDialog.getSaveFileName(self, 'Save File', str(CONF.well_dir))
        self.file_path_lineEdit.setText(fl)
