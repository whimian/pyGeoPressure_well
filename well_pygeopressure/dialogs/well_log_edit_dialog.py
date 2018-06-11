# -*- coding: utf-8 -*-
"""
Log Edit Dialog

Created on Mon Jun 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from PyQt4.QtGui import (QIcon, QDialog, QGridLayout, QTableWidget,
                         QTableWidgetItem, QDialogButtonBox, QMessageBox)

import well_pygeopressure.ui.resources_rc

from well_pygeopressure.config import CONF
import pygeopressure as ppp


class WellLogEditDialog(QDialog):
    def __init__(self, current_well_name, current_log_name):
        super(WellLogEditDialog, self).__init__()
        self.well = ppp.Well(
            str(CONF.well_dir / ".{}".format(current_well_name)))
        self.current_log_name = current_log_name
        self.well_log = self.well.get_log(current_log_name)

        self.resize(300, 400)
        self.initUI()
        self.button_box.accepted.connect(self.save_edit)
        self.button_box.rejected.connect(self.close)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        self.setWindowTitle("Edit Log {}".format(self.current_log_name))
        self.layout = QGridLayout(self)
        # add a QTableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Depth"))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Data"))
        n = len(self.well_log.depth)
        self.tableWidget.setRowCount(n)
        for i, (de, da) in enumerate(zip(self.well_log.depth, self.well_log.data)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(de)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(da)))
        self.layout.addWidget(self.tableWidget)
        # add QDialogButtonBox
        self.button_box = QDialogButtonBox(self)
        self.button_box.setStandardButtons(
            QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)

    def save_edit(self):
        depth_tb = [float(self.tableWidget.item(irow, 0).text()) \
            for irow in range(self.tableWidget.rowCount())]
        data_tb = [float(self.tableWidget.item(irow, 1).text()) \
            for irow in range(self.tableWidget.rowCount())]
        temp_log = ppp.Log()
        temp_log.depth = depth_tb
        temp_log.data = data_tb
        if temp_log != self.well_log:
            reply = QMessageBox.question(
                self, "Save",
                "Log Data has been edited,\nAre you willing to save changes?",
                QMessageBox.Yes, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.well.update_log(self.current_log_name, temp_log)
                self.well.save_well()
        self.close()
