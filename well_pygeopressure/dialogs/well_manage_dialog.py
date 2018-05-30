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
                         QTableWidgetItem, QGridLayout, )
from PyQt4.QtCore import Qt, pyqtSlot, QSize

from well_pygeopressure.ui.ui_well_manage_dialog import Ui_well_manage_Dialog
from well_pygeopressure.dialogs.well_log_view_dialog import WellLogViewDialog
from well_pygeopressure.dialogs.well_marker_dialog import WellMarkerDialog

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
        # self.selectButton.clicked.connect(self.on_clicked_selectButton)

    def initUI(self):
        # self.setWindowIcon(QIcon(':/icon/data_icon'))

        self.populate_well_listWidget()
        # self.rename_well_Button.setIcon(QIcon(':/icon/rename_icon'))
        # self.rename_well_Button.setIconSize(QSize(20, 20))
        # self.delete_well_Button.setIcon(QIcon(':/icon/delete_icon'))
        # self.delete_well_Button.setIconSize(QSize(20, 20))
        # self.import_well_Button.setIcon(QIcon(':/icon/import_icon'))
        # self.import_well_Button.setIconSize(QSize(20, 20))
        # self.layer_well_Button.setIcon(QIcon(':/icon/layer_icon'))
        # self.layer_well_Button.setIconSize(QSize(20, 20))
        # # ---
        # self.rename_log_Button.setIcon(QIcon(':/icon/rename_icon'))
        # self.rename_log_Button.setIconSize(QSize(20, 20))
        # self.delete_log_Button.setIcon(QIcon(':/icon/delete_icon'))
        # self.delete_log_Button.setIconSize(QSize(20, 20))
        # self.view_log_Button.setIcon(QIcon(':/icon/view_icon'))
        # self.view_log_Button.setIconSize(QSize(20, 20))
        # self.import_log_Button.setIcon(QIcon(':/icon/import_icon'))
        # self.import_log_Button.setIconSize(QSize(20, 20))
        # self.edit_log_Button.setIcon(QIcon(':/icon/edit_icon'))
        # self.edit_log_Button.setIconSize(QSize(20, 20))
        # self.create_log_Button.setIcon(QIcon(':/icon/create_icon'))
        # self.create_log_Button.setIconSize(QSize(20, 20))

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

    def open_marker_edit_dialog(self):
        well = ppp.Well(
            str(CONF.well_dir / ".{}".format(
                self.wells_listWidget.currentItem().text())))
        marker_edit_dialog = WellMarkerDialog(well)
        marker_edit_dialog.exec_()
