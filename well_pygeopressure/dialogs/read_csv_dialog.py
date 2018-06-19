# -*- coding: utf-8 -*-
"""
Read Multiple Wells from File Dialog

Created on Tue May 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QListWidgetItem,
                         QTableWidgetItem, QGridLayout, QTextEdit,
                         QLabel, QLineEdit, QPushButton, QSpinBox)
from PyQt4.QtCore import Qt, pyqtSlot, pyqtSignal, QRect

from well_pygeopressure.ui.ui_read_csv_dialog import (
    Ui_read_csv_Dialog)
from well_pygeopressure.dialogs.format_definition_dialog import (
    FormatDefinitionDialog)
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc
from pandas import DataFrame

import pygeopressure as ppp


class ReadCsvDialog(QDialog, Ui_read_csv_Dialog):

    file_read = pyqtSignal(list)

    def __init__(self):
        super(ReadCsvDialog, self).__init__()
        self.setupUi(self)
        self.initUI()

        self.fl_name = None
        self.definition = None

        self.defineButton.clicked.connect(self.open_definition_dialog)
        self.selectButton.clicked.connect(self.select_file)
        self.examineButton.clicked.connect(self.preview_file)
        self.buttonBox.accepted.connect(self.read_selected_file)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/icon'))


    def open_definition_dialog(self):
        format_dialog = FormatDefinitionDialog()
        format_dialog.format_defined.connect(self.set_definition)
        format_dialog.exec_()

    def select_file(self):
        self.fl_name = str(QFileDialog.getOpenFileName(self, "Open File"))
        self.file_lineEdit.setText(self.fl_name)

    def preview_file(self):
        preview_dialog = QDialog(self)
        preview_dialog.setWindowTitle("Preview file")
        preview_dialog.setMinimumSize(600, 400)
        # add a QTextEdit
        layout = QGridLayout(preview_dialog)
        file_textEdit = QTextEdit(preview_dialog)
        file_textEdit.setReadOnly(True)
        layout.addWidget(file_textEdit)
        # read file and display text in lineedit
        if self.fl_name:
            with open(self.fl_name, 'r') as fl:
                string_list = fl.readlines(20)
                file_textEdit.setText("\n".join(string_list))
            preview_dialog.exec_()

    @pyqtSlot(list)
    def set_definition(self, definition):
        self.definition = definition
        self.format_lineEdit.setText("<defined>")

    def read_selected_file(self):
        import pandas as pd
        df = pd.read_csv(
            self.fl_name, header=int(self.header_size_spinBox.value()-1),
            sep='\t')
        column_list = []
        for i in self.definition:
            if i is not None:
                column_list.append(df.columns[i])
        self.df = df[column_list]
        self.file_read.emit(self.df.values.tolist())
        self.close()
