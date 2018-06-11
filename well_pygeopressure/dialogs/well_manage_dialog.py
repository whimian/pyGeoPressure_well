# -*- coding: utf-8 -*-
"""
Well Management Dialog

Created on Tue May 10 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QListWidgetItem,
                         QTableWidgetItem, QGridLayout, QInputDialog,
                         QLineEdit, QMessageBox, QTableWidget,
                         QDialogButtonBox)
from PyQt4.QtCore import Qt, pyqtSlot, QSize

from well_pygeopressure.ui.ui_well_manage_dialog import Ui_well_manage_Dialog
from well_pygeopressure.dialogs.well_log_view_dialog import WellLogViewDialog
from well_pygeopressure.dialogs.well_marker_dialog import WellMarkerDialog
from well_pygeopressure.dialogs.import_multiple_wells_dialog import (
    ImportMultipleWellsDialog)
from well_pygeopressure.dialogs.import_logs_dialog import ImportLogsDialog

from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF

import well_pygeopressure.ui.resources_rc
import matplotlib.pyplot as plt

import pygeopressure as ppp


class WellManageDialog(QDialog, Ui_well_manage_Dialog):
    def __init__(self):
        super(WellManageDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.wells_listWidget.currentRowChanged.connect(
            self.populate_log_listWidget)
        self.wells_listWidget.currentRowChanged.connect(self.write_info)
        self.view_log_Button.clicked.connect(self.on_clicked_view_log_Button)
        self.layer_well_Button.clicked.connect(self.open_marker_edit_dialog)
        self.import_well_Button.clicked.connect(self.import_well)
        self.rename_log_Button.clicked.connect(self.rename_log)
        self.delete_log_Button.clicked.connect(self.delete_log)
        self.import_log_Button.clicked.connect(self.import_log)
        self.edit_log_Button.clicked.connect(self.edit_log)

    def initUI(self):
        self.populate_well_listWidget()

    def populate_well_listWidget(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            for name in get_data_files(CONF.well_dir):
                new_item = QListWidgetItem(name, self.wells_listWidget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)

    @pyqtSlot(int)
    def populate_log_listWidget(self, current_row):
        self.logs_listWidget.clear()
        current_item = self.wells_listWidget.item(current_row)
        well = ppp.Well(str(CONF.well_dir / ".{}".format(current_item.text())))
        self.logs_listWidget.addItems(well.logs)

    @pyqtSlot(int)
    def write_info(self, current_row):
        current_item = self.wells_listWidget.item(current_row)
        well = ppp.Well(str(CONF.well_dir / ".{}".format(current_item.text())))
        info_string = \
            "Surface coordinate: ({}, {})\n".format(
                well.loc[0], well.loc[1]) + \
            "Reference Datum Elevation [KB]: {}m\n".format(
                well.kelly_bushing) + \
            "Total Depth [TD]: {}m\n".format(well.total_depth) + \
            "Replacement velocity [from KB to SRD]: 2000m/s"
        self.info_textEdit.setPlainText(info_string)
        self.show_more_info(well)

    def show_more_info(self, well):
        # clear table
        while self.saved_info_tableWidget.rowCount() > 0:
            self.saved_info_tableWidget.removeRow(0)

        normal_keys = ["KB", "WD", "TD", "loc", "hdf_file", "well_name", "horizon"]
        for i in range(self.saved_info_tableWidget.rowCount()):
            self.saved_info_tableWidget.removeRow(i)
        for name in well.params.keys():
            if name not in normal_keys:
                self.saved_info_tableWidget.insertRow(0)
                self.saved_info_tableWidget.setItem(
                    0, 0, QTableWidgetItem(name))
                self.saved_info_tableWidget.setItem(
                    0, 1, QTableWidgetItem(str(well.params[name])))
        self.saved_info_tableWidget.sortItems(0, Qt.AscendingOrder)


    # WELL PANEL --------------------------------------------------------------
    def rename_well(self):
        pass

    def delete_well(self):
        pass

    def import_well(self):
        import_multiple_wells_dialog = ImportMultipleWellsDialog()
        import_multiple_wells_dialog.exec_()

    def export_well(self):
        pass

    def open_marker_edit_dialog(self):
        well = ppp.Well(
            str(CONF.well_dir / ".{}".format(
                self.wells_listWidget.currentItem().text())))
        marker_edit_dialog = WellMarkerDialog(well)
        marker_edit_dialog.exec_()

    # LOG PANEL ---------------------------------------------------------------
    def rename_log(self):
        if self.logs_listWidget.currentItem() is not None:
            well = ppp.Well(
                str(CONF.well_dir / ".{}".format(
                    self.wells_listWidget.currentItem().text())))
            current_log_name = str(self.logs_listWidget.currentItem().text())

            text, ok = QInputDialog.getText(
                self, "Rename Log", "Rename '{}'".format(current_log_name),
                QLineEdit.Normal, current_log_name)
            if ok and text:
                new_log_name = str(text)
                well.rename_log(current_log_name, new_log_name)
                well.save_well()
                # old_current = self.wells_listWidget.currentRow()
                # self.populate_well_listWidget()
                # self.wells_listWidget.setCurrentRow(old_current)
                self.populate_log_listWidget(self.wells_listWidget.currentRow())

    def delete_log(self):
        if self.logs_listWidget.currentItem() is not None:
            well = ppp.Well(
                str(CONF.well_dir / ".{}".format(
                    self.wells_listWidget.currentItem().text())))
            current_log_name = str(self.logs_listWidget.currentItem().text())

            reply = QMessageBox.question(
                self, "Delete Log",
                "Are you sure to delete log \n'{}'?".format(current_log_name),
                QMessageBox.Yes, QMessageBox.Cancel)

            if reply == QMessageBox.Yes:
                well.drop_log(current_log_name)
                well.save_well()
                self.populate_log_listWidget(self.wells_listWidget.currentRow())

    def import_log(self):
        current_well = self.wells_listWidget.currentItem().text()
        import_logs_dialog = ImportLogsDialog(current_well)
        import_logs_dialog.exec_()

    def export_log(self):
        pass

    def on_clicked_view_log_Button(self):
        if self.logs_listWidget.currentItem() is not None:
            well = ppp.Well(
                str(CONF.well_dir / ".{}".format(
                    self.wells_listWidget.currentItem().text())))
            well_log = well.get_log(
                str(self.logs_listWidget.currentItem().text()))
            # create a viewer on the fly
            viewer = WellLogViewDialog(well_log)
            viewer.exec_()

    def edit_log(self):
        if self.logs_listWidget.currentItem() is not None:
            well = ppp.Well(
                str(CONF.well_dir / ".{}".format(
                    self.wells_listWidget.currentItem().text())))
            current_log_name = str(self.logs_listWidget.currentItem().text())
            well_log = well.get_log(current_log_name)

            self.edit_dialog = QDialog(self)
            self.edit_dialog.setWindowTitle("Edit Log {}".format(current_log_name))
            # add a QTableWidget
            layout = QGridLayout(self.edit_dialog)
            tableWidget = QTableWidget(self.edit_dialog)
            tableWidget.setColumnCount(2)
            tableWidget.setRowCount(0)
            tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Depth"))
            tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Data"))
            layout.addWidget(tableWidget)
            button_box = QDialogButtonBox(self.edit_dialog)
            button_box.setStandardButtons(
                QDialogButtonBox.Save|QDialogButtonBox.Cancel)
            layout.addWidget(button_box)
            n = len(well_log.depth)
            tableWidget.setRowCount(n)
            for i, (de, da) in enumerate(zip(well_log.depth, well_log.data)):
                tableWidget.setItem(i, 0, QTableWidgetItem(str(de)))
                tableWidget.setItem(i, 1, QTableWidgetItem(str(da)))
            # tableWidget.sortItems(0, Qt.AscendingOrder)
            button_box.accepted.connect(self.save_edit)
            button_box.rejected.connect(self.edit_dialog.close)
            self.edit_dialog.exec_()

    def save_edit(self):
        well = ppp.Well(
            str(CONF.well_dir / ".{}".format(
                self.wells_listWidget.currentItem().text())))
        current_log_name = str(self.logs_listWidget.currentItem().text())
        well_log = well.get_log(current_log_name)
        tableWidget = self.edit_dialog.findChild(QTableWidget)
        depth_tb = [float(tableWidget.item(irow, 0).text()) \
            for irow in range(tableWidget.rowCount())]
        data_tb = [float(tableWidget.item(irow, 1).text()) \
            for irow in range(tableWidget.rowCount())]
        temp_log = ppp.Log()
        temp_log.depth = depth_tb
        temp_log.data = data_tb
        if temp_log != well_log:
            reply = QMessageBox.question(
                self, "Save",
                "Log Data has been edited,\nAre you willing to save changes?",
                QMessageBox.Yes, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                well.update_log(current_log_name, temp_log)
                well.save_well()
        self.edit_dialog.close()

    def create_log(self):
        pass
