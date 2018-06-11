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
                         QFileDialog, QComboBox, QListWidget, QListWidgetItem,
                         QCheckBox)
from PyQt4.QtCore import Qt, QRect, QSize
import well_pygeopressure.ui.resources_rc

from well_pygeopressure.config import CONF
from well_pygeopressure.basic.utils import get_data_files
import pygeopressure as ppp


class WellExportDialog(QDialog):
    def __init__(self):
        super(WellExportDialog, self).__init__()
        self.resize(400, 300)
        self.initUI()
        self.export_Button.clicked.connect(self.export_well)
        self.button_box.rejected.connect(self.close)
        self.select_Button.clicked.connect(self.select_file)
        self.well_comboBox.currentIndexChanged.connect(
            self.populate_log_listWidget)

        self.update_well_comboBox()

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/export'))
        self.setWindowTitle("Export Well")
        self.layout = QGridLayout(self)
        # add QLabel
        self.label_0 = QLabel(self)
        self.label_0.setGeometry(QRect(0, 24, 31, 20))
        self.label_0.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_0.setText("Well to export:")
        self.layout.addWidget(self.label_0, 0, 0)
        # add QComboBox
        self.well_comboBox = QComboBox(self)
        self.well_comboBox.setGeometry(QRect(10, 10, 101, 24))
        self.layout.addWidget(self.well_comboBox, 0, 1, 1, 1)
        # add QCheckBox
        self.checkbox = QCheckBox(self)
        self.checkbox.setText("Full LAS")
        self.checkbox.setCheckState(Qt.Unchecked)
        self.layout.addWidget(self.checkbox, 0, 2)
        # add QListWidget
        self.logs_listWidget = QListWidget(self)
        self.logs_listWidget.setGeometry(QRect(0, 0, 101, 201))
        # self.well_comboBox.setMaximumHeight(151)
        self.layout.addWidget(self.logs_listWidget, 1, 1)
        # add QLabel
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(QRect(0, 24, 31, 20))
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_1.setText("Output File:")
        self.layout.addWidget(self.label_1, 2, 0)
        # add QLineEdit
        self.file_path_lineEdit = QLineEdit(self)
        self.file_path_lineEdit.setGeometry(QRect(50, 24, 81, 20))
        self.layout.addWidget(self.file_path_lineEdit, 2, 1)
        # add Button
        self.select_Button = QPushButton(self)
        self.select_Button.setMaximumSize(QSize(61, 24))
        self.select_Button.setText("Select")
        self.layout.addWidget(self.select_Button, 2, 2)
        # add QDialogButtonBox
        self.button_box = QDialogButtonBox(self)
        self.export_Button = self.button_box.addButton(
            "Export", QDialogButtonBox.ApplyRole)
        self.button_box.addButton(QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box, 3, 0, 1, 3)

    def update_well_comboBox(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            dnames = get_data_files(CONF.well_dir)
            self.well_comboBox.addItems(dnames)

    def populate_log_listWidget(self):
        self.logs_listWidget.clear()
        well = ppp.Well(
            str(CONF.well_dir / ".{}".format(self.well_comboBox.currentText())))
        # self.logs_listWidget.addItems(well.logs)
        for name in well.logs:
            new_item = QListWidgetItem(name, self.logs_listWidget)
            new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
            new_item.setCheckState(Qt.Unchecked)

    def export_well(self):
        file_name = str(self.file_path_lineEdit.text())
        if not file_name:
            QMessageBox().information(self, "Info", "Please select ouput file.")
            pass
        else:
            well = well = ppp.Well(
                str(CONF.well_dir / ".{}".format(
                    self.well_comboBox.currentText())))
            logs_to_export = []
            for i in range(self.logs_listWidget.count()):
                item = self.logs_listWidget.item(i)
                if item.checkState() == Qt.Checked:
                    logs_to_export.append(str(item.text()))
            full = True if self.checkbox.checkState() == Qt.Checked \
                else False
            well.export(file_name, logs_to_export, full)
            QMessageBox().information(self, "Info", "Succeed!")

    def select_file(self):
        fl = QFileDialog.getSaveFileName(self, 'Save File', str(CONF.well_dir))
        self.file_path_lineEdit.setText(fl)
