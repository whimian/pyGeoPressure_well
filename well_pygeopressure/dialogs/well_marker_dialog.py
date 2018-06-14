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
        pass


# class OpenMarkersFileDialog(
#         QDialog, Ui_read_multiple_wells_from_file_Dialog):

#     file_read = pyqtSignal(list)

#     def __init__(self):
#         super(ReadMultipleWellsFromFileDialog, self).__init__()
#         self.setupUi(self)
#         self.initUI()

#         self.fl_name = None
#         self.definition = None

#         self.defineButton.clicked.connect(self.open_definition_dialog)
#         self.selectButton.clicked.connect(self.select_file)
#         self.examineButton.clicked.connect(self.preview_file)
#         self.buttonBox.accepted.connect(self.read_selected_file)

#     def initUI(self):
#         self.setWindowIcon(QIcon(':/icon/icon'))

#     def open_definition_dialog(self):
#         format_dialog = FormatDefinitionDialog()
#         format_dialog.format_defined.connect(self.set_definition)
#         format_dialog.exec_()

#     def select_file(self):
#         self.fl_name = str(QFileDialog.getOpenFileName(self, "Open File"))
#         self.file_lineEdit.setText(self.fl_name)

#     def preview_file(self):
#         preview_dialog = QDialog(self)
#         preview_dialog.setWindowTitle("Preview file")
#         preview_dialog.setMinimumSize(600, 400)
#         # add a QTextEdit
#         layout = QGridLayout(preview_dialog)
#         file_textEdit = QTextEdit(preview_dialog)
#         file_textEdit.setReadOnly(True)
#         layout.addWidget(file_textEdit)
#         # read file and display text in lineedit
#         with open(self.fl_name, 'r') as fl:
#             string_list = fl.readlines(20)
#             file_textEdit.setText("\n".join(string_list))
#         preview_dialog.exec_()

#     @pyqtSlot(list)
#     def set_definition(self, definition):
#         self.definition = definition
#         self.format_lineEdit.setText("<defined>")

#     def read_selected_file(self):
#         import pandas as pd
#         df = pd.read_csv(
#             self.fl_name, header=int(self.header_size_spinBox.value()-1),
#             sep='\t')
#         column_list = []
#         for i in self.definition:
#             if i is not None:
#                 column_list.append(df.columns[i])
#         self.df = df[column_list]
#         self.file_read.emit(self.df.values.tolist())
#         self.close()
