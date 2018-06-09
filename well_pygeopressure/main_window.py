# -*- coding: utf-8 -*-
"""
A GUI application for geopressure prediction

Created on Fri Jan 05 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import super, str

__author__ = "Yu Hao"

# Stdlib imports --------------------------------------------------------------
import sys
import time
import json
# Qt imports ------------------------------------------------------------------
from PyQt4.QtGui import (QIcon, QApplication, QMainWindow, QMessageBox,
                         QGridLayout, QListWidgetItem, QWidget,
                         QProgressBar)
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import Qt, pyqtSignal, pyqtSlot
# -----------------------------------------------------------------------------
# try:
#     _fromUtf8 = QtCore.QString.fromUtf8
# except AttributeError:
#     def _fromUtf8(s):
#         return s
# try:
#     _encoding = QApplication.UnicodeUTF8
#     def _translate(context, text, disambig):
#         return QApplication.translate(context, text, disambig, _encoding)
# except AttributeError:
#     def _translate(context, text, disambig):
#         return QApplication.translate(context, text, disambig)
# Third Party imports ---------------------------------------------------------
import numpy as np
from pathlib2 import Path
# Local imports ---------------------------------------------------------------
import pygeopressure as ppp

from well_pygeopressure.ui.ui_main_window import Ui_MainWindow
import well_pygeopressure.ui.resources_rc
# import Dialogs
from well_pygeopressure.dialogs.survey_edit_dialog import SurveyEditDialog
from well_pygeopressure.dialogs.survey_select_dialog import SurveySelectDialog
from well_pygeopressure.dialogs.well_manage_dialog import WellManageDialog
from well_pygeopressure.dialogs.import_multiple_wells_dialog import (
    ImportMultipleWellsDialog)
from well_pygeopressure.dialogs.import_logs_dialog import ImportLogsDialog
from well_pygeopressure.dialogs.nct_dialog import NctDialog
from well_pygeopressure.dialogs.discern_shale_dialog import DiscernShaleDialog
from well_pygeopressure.dialogs.upscale_dialog import UpscaleDialog
from well_pygeopressure.dialogs.smooth_dialog import SmoothDialog
from well_pygeopressure.dialogs.extrapolate_dialog import ExtrapolateDialog
from well_pygeopressure.dialogs.obp_dialog import ObpDialog
from well_pygeopressure.dialogs.optimize_eaton_dialog import (
    OptimizeEatonDialog)
from well_pygeopressure.dialogs.eaton_dialog import (
    EatonDialog)
from well_pygeopressure.dialogs.optimize_bowers_dialog import (
    OptimizeBowersDialog)
from well_pygeopressure.dialogs.bowers_dialog import (
    BowersDialog)
# # import Views
from well_pygeopressure.views.map_view import MapView
from well_pygeopressure.basic.utils import (get_data_files, Seismic,
                                            create_new_seismic_file)

from well_pygeopressure.config import CONF

# Main Window =================================================================
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.program_setting = None
        self.setupUi(self)
        self.initUI()
        # connect slots -------------------------------------------------------
        # menu actions
        self.actionNewSurvey.triggered.connect(self.create_survey_edit_dialog)
        self.actionSelectSurvey.triggered.connect(
            self.create_survey_select_dialog)
        self.actionAbout.triggered.connect(self.show_about)
        self.actionManage_wells.triggered.connect(
            self.create_well_manage_dialog)
        self.actionImport_Multiple.triggered.connect(
            self.create_import_multiple_wells_dialog)
        self.actionImport.triggered.connect(
            self.create_import_logs_dialog)
        self.actionDiscern_Shale.triggered.connect(self.create_shale_dialog)
        self.actionNCT.triggered.connect(self.create_nct_dialog)
        self.actionSmooth_Log.triggered.connect(
            self.create_smooth_dialog)
        self.actionUpscale_Log.triggered.connect(
            self.create_upscale_dialog)
        self.actionExtrapolate_Log.triggered.connect(
            self.create_extrapolate_dialog)
        self.actionOBP.triggered.connect(self.create_obp_dialog)
        self.actionOptimize_Eaton.triggered.connect(
            self.create_optimize_eaton_dialog)
        self.actionEaton.triggered.connect(
            self.create_eaton_dialog)
        self.actionOptimize_Bowers.triggered.connect(
            self.create_optimize_bowers_dialog)
        self.actionBowers.triggered.connect(
            self.create_bowers_dialog)
        # # toolbox
        # # update ui
        # self.toolBox.currentChanged.connect(
        #     self.update_velocity_conversion_panel)
        # self.toolBox.currentChanged.connect(self.update_tdc_panel)
        # self.toolBox.currentChanged.connect(self.update_density_panel)
        # self.toolBox.currentChanged.connect(self.update_obp_panel)
        # self.toolBox.currentChanged.connect(self.update_eaton_panel)
        # self.toolBox.currentChanged.connect(self.update_bowers_panel)
        # # buttons
        # self.runButton_Velocity_Conversion.clicked.connect(
        #     self.run_velocity_conversion)
        # self.runButton_gardner.clicked.connect(self.run_density_conversion)
        # self.runButton_OBP.clicked.connect(self.run_obp_calculation)
        # self.runButton_Eaton.clicked.connect(self.run_eaton_calculation)
        # self.runButton_Bowers.clicked.connect(self.run_bowers_calculation)

        # # Data Tree
        self.data_listWidget.itemClicked.connect(self.handleItemChecked)
        # # self.statusBar().showMessage("System Status | Normal")
        # self.source = None

    def initUI(self):
        # self.setWindowIcon(QIcon(':/icon/icon'))
        self.setWindowTitle("Well GeoPressure V1.0")

        self.populate_data_list()
        self.create_map_view()
        self.show()

    @pyqtSlot()
    def handleItemChecked(self):
        # self.statusBar().showMessage("evoked", msecs=50)
        x, y, well_names = [], [], []
        for idx in range(self.data_listWidget.count()):
            item = self.data_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                well = ppp.Well(str(CONF.well_dir / ".{}".format(item.text())))
                x.append(well.loc[0])
                y.append(well.loc[1])
                well_names.append(item.text())
        self.map_view.draw_well_loc(x, y, well_names)


    def create_map_view(self):
        layout = QGridLayout(self.tab_map)
        self.map_view = MapView(self.tab_map)
        layout.addWidget(self.map_view)
        self.update_map_view()

    def update_map_view(self):
        file_path = CONF.survey_dir / ".survey"
        if file_path.exists():
            self.map_view.draw_map(
                ppp.SurveySetting(
                    ppp.ThreePoints(str(file_path))))

    @pyqtSlot()
    def populate_data_list(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            for name in get_data_files(CONF.well_dir):
                new_item = QListWidgetItem(name, self.data_listWidget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)

    @pyqtSlot()
    def show_about(self):
        QMessageBox.about(
            self, "pyGeoPressue",
            "Well geopressure prediction.\n" + "\n" + \
            "Copyright: CUG\n" + \
            "Author: yuhao\n" + \
            "E-mail: yuhao89@live.cn")

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            save_config()
            event.accept()
        else:
            event.ignore()

    def create_survey_edit_dialog(self):
        survey_edit_window = SurveyEditDialog()
        survey_edit_window.exec_()

    def create_survey_select_dialog(self):
        survey_select_dialog = SurveySelectDialog()
        survey_select_dialog.selectButton.clicked.connect(
            self.populate_data_list)
        survey_select_dialog.exec_()

    @pyqtSlot()
    def create_well_manage_dialog(self):
        self.well_manage_dialog = WellManageDialog()
        self.well_manage_dialog.exec_()

    @pyqtSlot()
    def create_import_multiple_wells_dialog(self):
        import_multiple_wells_dialog = ImportMultipleWellsDialog()
        import_multiple_wells_dialog.exec_()

    def create_import_logs_dialog(self):
        import_logs_dialog = ImportLogsDialog()
        import_logs_dialog.exec_()

    def create_nct_dialog(self):
        nct_dialog = NctDialog()
        nct_dialog.exec_()

    def create_shale_dialog(self):
        shale_dialog = DiscernShaleDialog()
        shale_dialog.exec_()

    def create_smooth_dialog(self):
        smooth_dialog = SmoothDialog()
        smooth_dialog.exec_()

    def create_upscale_dialog(self):
        upscale_dialog = UpscaleDialog()
        upscale_dialog.exec_()

    def create_extrapolate_dialog(self):
        extrapolate_dialog = ExtrapolateDialog()
        extrapolate_dialog.exec_()

    def create_obp_dialog(self):
        obp_dialog = ObpDialog()
        obp_dialog.exec_()

    def create_optimize_eaton_dialog(self):
        optimize_eaton_dialog = OptimizeEatonDialog()
        optimize_eaton_dialog.exec_()

    def create_eaton_dialog(self):
        eaton_dialog = EatonDialog()
        eaton_dialog.exec_()

    def create_optimize_bowers_dialog(self):
        optimize_bowers_dialog = OptimizeBowersDialog()
        optimize_bowers_dialog.exec_()

    def create_bowers_dialog(self):
        bowers_dialog = BowersDialog()
        bowers_dialog.exec_()

def save_config():
    survey_path = Path(CONF.data_root) / CONF.current_survey
    if survey_path.exists():
        CONF.to_json(CONF.setting_abs_path)

def start():
    # app = QApplication.instance()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
