# -*- coding: utf-8 -*-
"""
Import Multiple Wells Dialog

Created on Tue May 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

import json
from pathlib2 import Path

from PyQt4.QtGui import (QIcon, QDialog, QTableWidgetItem, QMessageBox)
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_import_multiple_wells_dialog import (
    Ui_import_multiple_wells_Dialog)
from well_pygeopressure.dialogs.read_multiple_wells_from_file_dialog import (
    ReadMultipleWellsFromFileDialog)
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
import well_pygeopressure.ui.resources_rc

import pygeopressure as ppp


class ImportMultipleWellsDialog(QDialog, Ui_import_multiple_wells_Dialog):
    def __init__(self):
        super(ImportMultipleWellsDialog, self).__init__()
        self.setupUi(self)
        self.initUI()

        self.openButton.clicked.connect(self.open_read_from_file_dialog)
        self.createButton.clicked.connect(self.create_multiple_wells)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/icon'))
        # self.populate_marker_table()

    def open_read_from_file_dialog(self):
        read_multiple = ReadMultipleWellsFromFileDialog()
        read_multiple.file_read.connect(self.display_wells)
        read_multiple.exec_()

    @pyqtSlot(list)
    def display_wells(self, well_list):
        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

        for item in well_list:
            self.tableWidget.insertRow(0)
            for i, value in enumerate(item):
                self.tableWidget.setItem(
                    0, i, QTableWidgetItem(str(value)))
                if i == 0:
                    new_item = self.tableWidget.item(0, 0)
                    new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                    new_item.setCheckState(Qt.Unchecked)
        # self.tableWidget.sortItems(0, Qt.AscendingOrder)
        # add other item
        for irow in range(self.tableWidget.rowCount()):
            for icol in range(6):
                if self.tableWidget.item(irow, icol) is None:
                    self.tableWidget.setItem(irow, icol, QTableWidgetItem(""))

    def create_multiple_wells(self):
        for irow in range(self.tableWidget.rowCount()):
            well_name_item = self.tableWidget.item(irow, 0)
            if well_name_item.checkState() == Qt.Checked:
                new_dict = {}
                new_dict["well_name"] = str(
                    self.tableWidget.item(irow, 0).text())
                new_dict["loc"] = [
                    float(str(self.tableWidget.item(irow, 1).text())),
                    float(str(self.tableWidget.item(irow, 2).text()))]
                kb = str(self.tableWidget.item(irow, 3).text())
                new_dict["KB"] = float(kb) if kb else 0
                wd = str(self.tableWidget.item(irow, 4).text())
                new_dict["WD"] = float(wd) if wd else 0
                td = str(self.tableWidget.item(irow, 5).text())
                new_dict["TD"] = float(td) if wd else 0

                hdf_file = CONF.well_dir / "well_data.h5"
                if not hdf_file.exists():
                    hdf_file.touch()
                new_dict["hdf_file"] = str(hdf_file)

                well_file = CONF.well_dir / ".{}".format(new_dict["well_name"])
                if well_file.exists():
                    QMessageBox.warning(
                        self, "Message",
                        "{} already existed.".format(new_dict["well_name"]))
                else:
                    well_file.touch()
                    with open(str(well_file), "w") as fl:
                        json.dump(new_dict, fl, indent=4)

        QMessageBox.information(self, "Message", "{}".format("Succeed!"))
