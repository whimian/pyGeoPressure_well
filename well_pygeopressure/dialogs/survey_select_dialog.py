# -*- coding: utf-8 -*-
"""
A survey setting class

Created on Sat Jan 20 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from future.builtins import str as newstr

from pathlib2 import Path
from PyQt4.QtGui import QIcon, QDialog, QFileDialog
from PyQt4 import uic, QtCore

from ..basic.utils import get_available_survey_dir
# from ..basic.survey_setting import SurveySetting
from ..widgets.survey_map_widget import SurveyMap
from ..ui.ui_survey_select import Ui_surveySelectDialog

from well_pygeopressure.config import CONF
import pygeopressure as ppp


class SurveySelectDialog(QDialog, Ui_surveySelectDialog):
    def __init__(self):
        super(SurveySelectDialog, self).__init__()
        self.setupUi(self)
        self.initUI()
        # connect
        self.surveyListWidget.itemSelectionChanged.connect(
            self.display_map_and_info)
        self.surveyButton.clicked.connect(self.on_clicked_surveyButton)
        self.selectButton.clicked.connect(self.on_clicked_selectButton)

        self.load_survey_list()

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/survey_icon'))
        self.survey_map = SurveyMap(self)
        self.gridLayout.addWidget(self.survey_map)
        self.show()

    def load_survey_list(self):
        if CONF.data_root is not None:
            self.dataRootLabel.setText(CONF.data_root)
            # populate surveylist
            dnames = get_available_survey_dir(Path(CONF.data_root))
            self.surveyListWidget.clear()
            self.surveyListWidget.addItems(dnames)

            if CONF.current_survey is not None:
                finded = self.surveyListWidget.findItems(
                    CONF.current_survey, QtCore.Qt.MatchExactly)
                if len(finded) != 0:
                    self.surveyListWidget.setItemSelected(finded[0], True)

    def on_clicked_surveyButton(self):
        # set new CONF.data_root
        CONF.data_root = str(QFileDialog.getExistingDirectory(
            self, "Select Directory"))
        # display CONF.data_root
        self.load_survey_list()

    def on_clicked_selectButton(self):
        CONF.current_survey = str(
            self.surveyListWidget.selectedItems()[0].text())
        self.done(1)

    def display_map_and_info(self):
        # get survey file path
        survey_folder = str(self.surveyListWidget.selectedItems()[0].text())
        survey_file = Path(CONF.data_root, survey_folder, '.survey')
        # create new survey
        new_survey = ppp.SurveySetting(ppp.ThreePoints(newstr(survey_file)))
        # build survey info string for display
        info_string = \
            "In-line range: {} - {} - {}\n".format(
                new_survey.startInline,
                new_survey.endInline,
                new_survey.stepInline) + \
            "Cross-line range: {} - {} - {}\n".format(
                new_survey.startCrline,
                new_survey.endCrline,
                new_survey.stepCrline) + \
            "Z range({}): {} - {} - {}\n".format(
                new_survey.startDepth,
                new_survey.endDepth,
                new_survey.stepDepth,
                new_survey.zType) + \
            "Inl/Crl bin size (m/line): {}/{}\n".format(
                new_survey.inline_bin,
                new_survey.crline_bin) + \
            "Area (sq km): {}; Survey type: Only 3D\n".format(
                new_survey.area) + \
            "In-line Orientation: {:.2f} Degrees from N\n".format(
                new_survey.azimuth) + \
            "Location: {}".format(str(Path(CONF.data_root, survey_folder)))
        self.surveyInfoTextEdit.setPlainText(info_string)
        # draw survey area plot
        inlines = [new_survey.startInline, new_survey.startInline,
                   new_survey.endInline, new_survey.endInline]
        crlines = [new_survey.startCrline, new_survey.endCrline,
                   new_survey.endCrline, new_survey.startCrline]
        x_c, y_c = new_survey.four_corner_on_canvas(
            self.survey_map.width(), self.survey_map.height())
        self.survey_map.inlines = inlines
        self.survey_map.crlines = crlines
        self.survey_map.x_canvas = x_c
        self.survey_map.y_canvas = y_c
        self.survey_map.repaint()
