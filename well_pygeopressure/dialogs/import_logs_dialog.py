# -*- coding: utf-8 -*-
"""
Import Logs Dialog

Created on Tue May 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QListWidgetItem,
                         QTableWidgetItem, QMessageBox)
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_import_logs_dialog import (
    Ui_import_logs_Dialog)
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import pygeopressure as ppp


class ImportLogsDialog(QDialog, Ui_import_logs_Dialog):
    def __init__(self, current_well = None):
        super(ImportLogsDialog, self).__init__()
        self.setupUi(self)
        self.current_well = current_well
        self.initUI()
        self.fl_name = None
        self.las_object = None
        self.selectButton.clicked.connect(self.select_file)
        self.importButton.clicked.connect(self.import_logs)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        self.populate_wells_comboBox()

    def populate_wells_comboBox(self):
        self.wells_comboBox.clear()
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            dnames = get_data_files(CONF.well_dir)
            self.wells_comboBox.addItems(dnames)
        if self.current_well is not None:
            index = self.wells_comboBox.findText(str(self.current_well))
            if index != -1:
                self.wells_comboBox.setCurrentIndex(index)

    @pyqtSlot()
    def select_file(self):
        fl = str(QFileDialog.getOpenFileName(self, "Open File"))
        if fl:
            self.fl_name = fl

            self.file_lineEdit.setText(self.fl_name)
            self.read_las_file()
            for name, unit in zip(self.logs, self.units):
                self.tableWidget.insertRow(0)
                self.tableWidget.setItem(
                    0, 0, QTableWidgetItem(name))
                new_item = self.tableWidget.item(0, 0)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)

                self.tableWidget.setItem(
                    0, 1, QTableWidgetItem(unit))

    def read_las_file(self):
        self.las_object = ppp.LasData(self.fl_name)
        self.data_frame = self.las_object.data_frame
        self.logs = self.las_object.logs
        self.units = self.las_object.units

    @pyqtSlot()
    def import_logs(self):
        # get the well into which logs will be imported
        well_name = self.wells_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        hdf_file = CONF.well_dir / "well_data.h5"
        # get logs to be imported
        # columns_to_import = ['Depth({})'.format(self.las_object.depth_unit),]
        columns_to_import = ['Depth(m)',]
        for irow in range(self.tableWidget.rowCount()):
            descr = self.tableWidget.item(irow, 0)
            if descr.checkState() == Qt.Checked:
                unit = self.tableWidget.item(irow, 1)
                columns_to_import.append("{}({})".format(descr.text(), unit.text()))
        df_import = self.data_frame[columns_to_import]
        try:
            # write to storage
            if well.in_hdf is False:
                storage = ppp.WellStorage(str(hdf_file))
                storage.add_well(str(well_name), df_import)
            else:
                storage = ppp.WellStorage(str(hdf_file))
                storage.logs_into_well(str(well_name), df_import)
            QMessageBox.information(self, "Message", "{}".format("Succeed!"))
        except Exception as ex:
            QMessageBox.warning(self, "Message", "{}".format(ex.message))
