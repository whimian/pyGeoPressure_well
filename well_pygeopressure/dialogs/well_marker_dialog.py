# -*- coding: utf-8 -*-
"""
Well Marker Edit Dialog

Created on Tue May 10 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement)

__author__ = "Yu Hao"

from pathlib2 import Path
from collections import OrderedDict

import pandas as pd
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QListWidgetItem,
                         QTableWidgetItem, QGridLayout, QDialogButtonBox,
                         QTableWidget, QMessageBox, QTextEdit)
from PyQt4.QtCore import Qt, pyqtSlot, pyqtSignal

from well_pygeopressure.dialogs.read_csv_dialog import ReadCsvDialog
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF

import well_pygeopressure.ui.resources_rc

import pygeopressure as ppp


class WellMarkerDialog(QDialog):
    def __init__(self, well):
        super(WellMarkerDialog, self).__init__()
        self.well = well
        self.setupUi()
        self.initUI()
        self.button_box.accepted.connect(self.save_markers)
        self.button_box.rejected.connect(self.close)
        self.add_Button.clicked.connect(self.add_row)
        self.del_Button.clicked.connect(self.del_row)
        self.export_Button.clicked.connect(self.export_markers)
        self.import_Button.clicked.connect(self.import_markers)

    def setupUi(self):
        self.resize(568, 411)
        self.setWindowIcon(QIcon(':/icon/layer_icon'))
        self.setWindowTitle("Edit Markers")
        self.gridLayout = QGridLayout(self)
        # table widget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderItem(
            0, QTableWidgetItem("Name"))
        self.tableWidget.setHorizontalHeaderItem(
            1, QTableWidgetItem("TVD (m)"))
        self.tableWidget.setHorizontalHeaderItem(
            2, QTableWidgetItem("TVDSS (m)"))
        self.tableWidget.setHorizontalHeaderItem(
            3, QTableWidgetItem("Color"))
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        # button box
        self.button_box = QDialogButtonBox(self)
        self.export_Button = self.button_box.addButton(
            "Export", QDialogButtonBox.ResetRole)
        self.import_Button = self.button_box.addButton(
            "Import", QDialogButtonBox.ResetRole)
        self.add_Button = self.button_box.addButton(
            "Add", QDialogButtonBox.ResetRole)
        self.del_Button = self.button_box.addButton(
            "Del", QDialogButtonBox.ResetRole)
        self.button_box.setStandardButtons(
            QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        self.gridLayout.addWidget(self.button_box, 1, 0, 1, 1)

    def initUI(self):
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

    def add_row(self):
        self.tableWidget.insertRow(self.tableWidget.rowCount())

    def del_row(self):
        self.tableWidget.removeRow(self.tableWidget.currentRow())

    def save_markers(self):
        l_names = [str(self.tableWidget.item(irow, 0).text()) \
            for irow in range(self.tableWidget.rowCount())]
        l_md = [float(self.tableWidget.item(irow, 1).text()) \
            for irow in range(self.tableWidget.rowCount())]
        new_dict = OrderedDict([(a, b) for a, b in zip(l_names, l_md)])
        if self.well.params['horizon'] != new_dict:
            respond = QMessageBox.question(
                self, "Save Markers", "Sure to save changes?",
                QMessageBox.Save | QMessageBox.Cancel)
            if respond == QMessageBox.Save:
                self.well.params['horizon'] = new_dict
                self.well.save_params()
        self.close()

    def export_markers(self):
        file_path = str(QFileDialog.getSaveFileName(self, "Save Markers"))
        l_names = [str(self.tableWidget.item(irow, 0).text()) \
            for irow in range(self.tableWidget.rowCount())]
        l_md = [float(self.tableWidget.item(irow, 1).text()) \
            for irow in range(self.tableWidget.rowCount())]
        df = pd.DataFrame({"name":l_names, "MD(m)":l_md})
        df.to_csv(file_path, sep='\t', columns=["name", "MD(m)"], index=False)
        QMessageBox.information(self, "Export Markers", "Succeed!")

    def import_markers(self):
        read_csv_dialog = ReadCsvDialog()
        read_csv_dialog.setWindowIcon(QIcon(':/icon/layer_icon'))
        read_csv_dialog.setWindowTitle("Open Markers File")
        read_csv_dialog.label.setText("Read Makers from File")
        read_csv_dialog.exec_()

