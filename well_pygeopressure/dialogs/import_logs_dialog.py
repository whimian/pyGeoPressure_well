# -*- coding: utf-8 -*-
"""
Import Logs Dialog

Created on Tue May 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QListWidgetItem, QTableWidgetItem
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_import_logs_dialog import (
    Ui_import_logs_Dialog)
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import pygeopressure as ppp


class ImportLogsDialog(QDialog, Ui_import_logs_Dialog):
    def __init__(self):
        super(ImportLogsDialog, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))
        # self.populate_marker_table()
