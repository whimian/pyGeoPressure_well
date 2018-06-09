# -*- coding: utf-8 -*-
"""
Survey info edit dialog

Created on Fri Jan 05 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
# from future.builtins import str

__author__ = "Yu Hao"

import sys

from PyQt4.QtGui import QIcon, QDialog, QFileDialog, QMessageBox, QWidget
from PyQt4 import uic

from well_pygeopressure.basic.utils import (read_survey_setting,
                                           discern_setting_from_gui,
                                           create_survey_directory,
                                           write_survey_file)
from well_pygeopressure.ui.ui_survey_edit import Ui_surveyEditDialog
from well_pygeopressure.config import CONF

from pathlib2 import Path


class SurveyEditDialog(QDialog, Ui_surveyEditDialog):
    def __init__(self):
        super(SurveyEditDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.temp_survey_dict = None
        # connect
        self.settingComboBox.currentIndexChanged.connect(self.load_from_file)
        self.applyButton.clicked.connect(self.create_new_survey)

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/survey_icon'))
        self.settingComboBox.addItems(['Enter Below',
                                       'From File'])
        self.unitComboBox.addItems(['msec', 'm'])
        self.surveyNameLineEdit.setText("new")
        self.surveyNameLineEdit.selectAll()
        self.show()

    def load_from_file(self):
        if self.settingComboBox.currentText() == 'From File':
            file_dlg = QFileDialog(self)
            file_dlg.setFileMode(QFileDialog.ExistingFile)
            file_dlg.setOption(QFileDialog.ReadOnly, True)

            file_dlg.setNameFilters(["coordinates (*.json)"])
            file_dlg.selectNameFilter("coordinates (*.json)")
            file_dlg.setDefaultSuffix("png")

            if file_dlg.exec_():
                filenames = file_dlg.selectedFiles()
                read_survey_setting(filenames[0], self)

    def create_new_survey(self):
        # read setting from the dialog
        self.temp_survey_dict = discern_setting_from_gui(self)

        new_path = Path(CONF.data_root) / self.temp_survey_dict["name"]
        if new_path.exists():
            # Show a message box
            w = QWidget()
            QMessageBox.information(w, "Warning", "Survey Name is Not Availible!\n \
                Choose another one.")
        else:
            create_survey_directory(Path(CONF.data_root),
                                    self.temp_survey_dict["name"])
            CONF.current_survey = self.temp_survey_dict["name"]

            write_survey_file(new_path / ".survey", self.temp_survey_dict)
            w = QWidget()
            QMessageBox.information(w, "Info", "Survey Creation Succeed!")
