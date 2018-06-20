# -*- coding: utf-8 -*-
"""
Import Logs Dialog

Created on Tue May 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"

from pathlib2 import Path
from PyQt4.QtGui import (QIcon, QDialog, QFileDialog, QMessageBox,
    QListWidgetItem, QTableWidgetItem, QGridLayout)
from PyQt4.QtCore import Qt, pyqtSlot

from well_pygeopressure.ui.ui_nct_dialog import (
    Ui_nct_Dialog)
from well_pygeopressure.widgets.matplotlib_widget import MatplotlibWidget
from well_pygeopressure.basic.utils import get_data_files
from well_pygeopressure.config import CONF
# import well_pygeopressure.qrc_resources
import well_pygeopressure.ui.resources_rc

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import pygeopressure as ppp


class NctDialog(QDialog, Ui_nct_Dialog):
    def __init__(self):
        super(NctDialog, self).__init__()
        self.setupUi(self)
        # connect
        self.well_comboBox.currentIndexChanged.connect(
            self.update_log_comboBox)
        self.well_comboBox.currentIndexChanged.connect(
            self.update_horizon_listWidget)
        self.well_comboBox.currentIndexChanged.connect(
            self.update_nct_tableWidget)
        # buttons
        self.plot_horizon_Button.clicked.connect(self.draw_horizon)
        self.plot_Button.clicked.connect(self.plot_button_on_clicked)
        self.draw_Button.clicked.connect(self.draw_line_with_a_b)
        self.fit_Button.clicked.connect(self.fit_button_on_clicked)
        self.clear_Button.clicked.connect(self.clear_lines)
        self.add_Button.clicked.connect(self.save_nct)
        self.delete_Button.clicked.connect(self.delete_nct)
        # checkboxs
        self.two_points_checkBox.stateChanged.connect(
            self.toggle_two_points_widgets)
        self.pick_checkBox.stateChanged.connect(self.toggle_pick_checkBox)
        self.initUI()

        self.P1 = []
        self.P2 = []
        self.norm_line_ax = []
        self.norm_line_ax2 = []
        # self.init_color_dict()
        self.color_dict = CONF.color_dict
        self.horizon_line = []
        self.connect_id = None # needed for matplotlib to connect with event

    def initUI(self):
        self.setWindowIcon(QIcon(':/icon/edit_icon'))

        self.matplotlib_widget = MatplotlibWidget(self)
        self.layout().insertWidget(1, self.matplotlib_widget)

        self.update_well_comboBox()
        self.init_axes()

        self.two_points_groupBox.setVisible(False)


    def update_well_comboBox(self):
        survey_file = CONF.survey_dir / '.survey'
        if survey_file.exists():
            dnames = get_data_files(CONF.well_dir)
            self.well_comboBox.addItems(dnames)

    def update_log_comboBox(self):
        self.log_comboBox.clear()
        self.sm_log_comboBox.clear()
        self.sh_log_comboBox.clear()
        well_name = self.well_comboBox.currentText()
        if well_name != "":
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            self.log_comboBox.addItems(well.logs)
            self.sm_log_comboBox.addItems(well.logs)
            self.sh_log_comboBox.addItems(well.logs)

    def update_horizon_listWidget(self):
        self.horizon_listWidget.clear()
        try:
            well_name = self.well_comboBox.currentText()
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
            horizons = well.params['horizon'].keys()
            # self.horizon_listWidget.addItems(horizons)
            for name in horizons:
                new_item = QListWidgetItem(name, self.horizon_listWidget)
                new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
                new_item.setCheckState(Qt.Unchecked)
        except KeyError as e:
            print(e.message)

    def draw_horizon(self):
        for line in self.horizon_line:
            del line

        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

        for idx in range(self.horizon_listWidget.count()):
            item = self.horizon_listWidget.item(idx)
            if item.checkState() == Qt.Checked:
                key = str(item.text())
                try:
                    color = self.color_dict[key]
                except KeyError:
                    color = 'black'
                self.horizon_line.append(
                    self.ax.axhline(y=well.params['horizon'][key],
                                    color=color, linewidth=0.5, zorder=0))
                self.horizon_line.append(
                    self.ax2.axhline(y=well.params['horizon'][key],
                                     color=color, linewidth=0.5, zorder=0))
                if 'T' in key:
                    import matplotlib.transforms as transforms
                    trans = transforms.blended_transform_factory(
                        self.ax.transAxes, self.ax.transData)
                    self.ax.text(
                        s=key, x=0.8, y=well.params['horizon'][key],
                        color=color, transform=trans, size=9)
                    trans2 = transforms.blended_transform_factory(
                        self.ax2.transAxes, self.ax2.transData)
                    self.ax2.text(
                        s=key, x=0.8, y=well.params['horizon'][key],
                        color=color, transform=trans2, size=9)
            self.matplotlib_widget.fig.canvas.draw()

    def update_nct_tableWidget(self):
        while self.nct_tableWidget.rowCount() > 0:
            self.nct_tableWidget.removeRow(0)

        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

        for name in well.params.keys():
            if "nct" in name:
                self.nct_tableWidget.insertRow(0)
                self.nct_tableWidget.setItem(
                    0, 0, QTableWidgetItem(name))
                self.nct_tableWidget.setItem(
                    0, 1, QTableWidgetItem(str(well.params[name]["a"])))
                self.nct_tableWidget.setItem(
                    0, 2, QTableWidgetItem(str(well.params[name]["b"])))
        self.nct_tableWidget.sortItems(0, Qt.AscendingOrder)

    def init_axes(self):
        self.matplotlib_widget.fig.delaxes(self.matplotlib_widget.axes)
        ax1 = self.matplotlib_widget.fig.add_subplot(121)
        self.matplotlib_widget.fig.add_subplot(122, sharey=ax1)
        self.matplotlib_widget.axes = self.matplotlib_widget.fig.axes
        self.ax = self.matplotlib_widget.axes[0]
        self.ax2 = self.matplotlib_widget.axes[1]
        plt.style.use(['seaborn-whitegrid', 'seaborn-paper'])
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False

    def toggle_two_points_widgets(self):
        if self.two_points_checkBox.checkState() == Qt.Checked:
            self.two_points_groupBox.setVisible(True)
        elif self.two_points_checkBox.checkState() == Qt.Unchecked:
            self.two_points_groupBox.setVisible(False)

    def reset_pick_points(self):
        self.two_points_checkBox.setCheckState(Qt.Unchecked)
        self.x_point1_lineEdit.setText(str(0))
        self.y_point1_lineEdit.setText(str(0))
        self.x_point2_lineEdit.setText(str(0))
        self.y_point2_lineEdit.setText(str(0))

        self.clear_points()
        self.clear_lines()

    def plot_button_on_clicked(self):
        self.reset_pick_points()
        # get logs
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

        vlog = well.get_log(str(self.log_comboBox.currentText()))
        sm_log = well.get_log(str(self.sm_log_comboBox.currentText()))
        sh_log = well.get_log(str(self.sh_log_comboBox.currentText()))

        depth = np.array(vlog.depth)
        vel = np.array(vlog.data)
        dt = vel**(-1)
        log_dt = np.log(dt)
        vel_sm = np.array(sm_log.data)
        dt_sm = 1/vel_sm
        log_dt_sm = np.log(dt_sm)
        vsh = np.array(sh_log.data)
        sand_mask = vsh < 0.35  # non-shale interval
        if self.shale_checkBox.checkState() == Qt.Unchecked:
            sand_mask = vsh > -99999
        # Loose Points -------------------------------------
        shale_vel_log = ppp.shale(vlog, vsh_log=sh_log, thresh=0.4)
        average_log = ppp.local_average(shale_vel_log)
        average_log = ppp.smooth_log(average_log)
        average_log = ppp.smooth_log(average_log)
        # smooth for two times
        average_data = np.array(average_log.data)
        average_dt = average_data**(-1)
        log_av_dt = np.log(average_dt)

        # Plot ----------------------------------------------------
        self.ax.cla()
        self.ax.plot(log_dt, depth, color='lightgray', zorder=0, linewidth=0.2)
        log_dt[sand_mask] = np.nan
        self.ax.plot(log_dt, depth, color='gray', linewidth=0.2, zorder=1)
        self.ax.plot(log_dt_sm, depth, zorder=2)
        # Shale Velocity
        self.ax.set(title=well.well_name,
                    xlabel=u"$\ln dt$", ylabel="Depth(MD) (m)")
        self.ax.set_ylim((5000, 0))
        # axis 2 -------------------------------------------------------
        self.ax2.cla()
        self.ax2.plot(vel, depth, color='lightgray', zorder=0, linewidth=0.2)
        vel[sand_mask] = np.nan
        self.ax2.plot(vel, depth, color='gray', linewidth=0.2, zorder=1)
        self.ax2.plot(vel_sm, depth, zorder=2)
        # Shale Velocity
        self.ax2.set(title=well.well_name, xlabel="Interval Velocity(m/s)")

        self.ax2.set_ylim((5000, 0))
        self.matplotlib_widget.fig.canvas.draw()

    def fit_button_on_clicked(self):
        # get well log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))
        # get interval for fitting
        if self.start_lineEdit.text() == "":
            fit_start = log.top
            self.start_lineEdit.setText("{}".format(fit_start))
        else:
            fit_start = float(self.start_lineEdit.text())

        if self.end_lineEdit.text() == "":
            fit_stop = log.bottom
            self.end_lineEdit.setText("{}".format(fit_stop))
        else:
            fit_stop = float(self.end_lineEdit.text())
        # do fitting
        start_idx = log.get_depth_idx(fit_start)
        stop_idx = log.get_depth_idx(fit_stop) + 1
        depth = np.array(log.depth[start_idx: stop_idx + 1])
        vel = np.array(log.data[start_idx: stop_idx + 1])
        dt = vel**(-1)
        dt_log = np.log(dt)
        mask = np.isfinite(dt_log)
        dt_log_finite = dt_log[mask]
        depth_finite = depth[mask]

        popt, pcov = curve_fit(ppp.normal_dt, depth_finite, dt_log_finite)
        a, b = popt
        self.a_lineEdit.setText("{}".format(a))
        self.b_lineEdit.setText("{}".format(b))
        # plot on graph
        new_dt_log = ppp.normal_dt(np.array(log.depth), a, b)
        new_dt = np.exp(new_dt_log)
        new_vel = new_dt**(-1)
        self.norm_line_ax.append(self.ax.plot(new_dt_log, log.depth, '--')[0])
        self.norm_line_ax2.append(self.ax2.plot(new_vel, log.depth, '--')[0])
        self.matplotlib_widget.fig.canvas.draw()

    def clear_lines(self):
        while self.norm_line_ax:
            self.norm_line_ax[-1].remove()
            del self.norm_line_ax[-1]
        while self.norm_line_ax2:
            self.norm_line_ax2[-1].remove()
            del self.norm_line_ax2[-1]

        self.matplotlib_widget.fig.canvas.draw()

    def clear_points(self):
        while self.P1:
            self.P1[-1].remove()
            del self.P1[-1]
        while self.P2:
            self.P2[-1].remove()
            del self.P2[-1]

    def draw_line_with_a_b(self):
        # get well log
        well_name = self.well_comboBox.currentText()
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))
        log = well.get_log(str(self.log_comboBox.currentText()))
        # get a, b
        a, b = float(self.a_lineEdit.text()), float(self.b_lineEdit.text())
        new_dt_log = a - b * np.array(log.depth)
        new_dt = np.exp(new_dt_log)
        new_vel = 1 / new_dt
        self.norm_line_ax.append(self.ax.plot(new_dt_log, log.depth, '--')[0])
        self.norm_line_ax2.append(self.ax2.plot(new_vel, log.depth, '--')[0])

        self.matplotlib_widget.fig.canvas.draw()

    def toggle_pick_checkBox(self):
        if self.pick_checkBox.checkState() == Qt.Checked:
            self.connect_id = self.matplotlib_widget.fig.canvas.mpl_connect(
                'button_press_event', self.on_press)
        elif self.pick_checkBox.checkState() == Qt.Unchecked and self.connect_id:
            self.matplotlib_widget.fig.canvas.mpl_disconnect(cid=self.connect_id)
            self.connect_id = None

    def on_press(self, event):
        """
        callback for matplotlib mouse clicked event
        """
        if self.point1_radioButton.isChecked():
            while self.P1:
                self.P1[-1].remove()
                del self.P1[-1]
            self.P1.append(
                self.ax.scatter(
                    x=[event.xdata], y=[event.ydata], color='red', zorder=100))
            self.matplotlib_widget.fig.canvas.draw()
            self.x_point1_lineEdit.setText("{}".format(event.xdata))
            self.y_point1_lineEdit.setText("{}".format(event.ydata))

            x_point1 = float(self.x_point1_lineEdit.text())
            y_point1 = float(self.y_point1_lineEdit.text())
            x_point2 = float(self.x_point2_lineEdit.text())
            y_point2 = float(self.y_point2_lineEdit.text())

            if x_point1 != 0 and y_point1 != 0 and \
                    x_point2 != 0 and y_point2 != 0:
                self.cal_line_param()
                self.clear_lines()
                self.draw_line_with_a_b()

        elif self.point2_radioButton.isChecked():
            while self.P2:
                self.P2[-1].remove()
                del self.P2[-1]
            self.P2.append(
                self.ax.scatter(
                    x=[event.xdata], y=[event.ydata], color='blue', zorder=10))
            self.matplotlib_widget.fig.canvas.draw()
            self.x_point2_lineEdit.setText("{}".format(event.xdata))
            self.y_point2_lineEdit.setText("{}".format(event.ydata))
            x_point1 = float(self.x_point1_lineEdit.text())
            y_point1 = float(self.y_point1_lineEdit.text())
            x_point2 = float(self.x_point2_lineEdit.text())
            y_point2 = float(self.y_point2_lineEdit.text())

            if x_point1 != 0 and y_point1 != 0 and \
                    x_point2 != 0 and y_point2 != 0:
                self.cal_line_param()
                self.clear_lines()
                self.draw_line_with_a_b()

    def cal_line_param(self):
        "calcualte a, b with two points selected on graph"
        ln_V1, ln_V2, d1, d2 = \
            float(self.x_point1_lineEdit.text()), \
            float(self.x_point2_lineEdit.text()), \
            float(self.y_point1_lineEdit.text()), \
            float(self.y_point2_lineEdit.text())
        popt, pcov = curve_fit(ppp.normal_dt, [d1, d2], [ln_V1, ln_V2])
        a, b = popt
        self.a_lineEdit.setText("{}".format(a))
        self.b_lineEdit.setText("{}".format(b))

    def save_nct(self):
        # get well
        well_name = str(self.well_comboBox.currentText())
        well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

        new_name = str(self.new_name_lineEdit.text())
        well.params[new_name] = {
            "a": float(self.a_lineEdit.text()),
            "b": float(self.b_lineEdit.text())
        }
        well.save_params()
        self.update_nct_tableWidget()

    def delete_nct(self):
        idx_row = self.nct_tableWidget.currentRow()
        reply = QMessageBox.question(
            self, 'Message',
            "Are you sure to delete {}?".format(
                self.nct_tableWidget.item(idx_row, 0).text()),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # remove
            key_to_delete = str(self.nct_tableWidget.item(idx_row, 0).text())
            # get well
            well_name = str(self.well_comboBox.currentText())
            well = ppp.Well(str(CONF.well_dir / ".{}".format(well_name)))

            del well.params[key_to_delete]
            well.save_params()

        else:
            # cancel
            pass
        self.update_nct_tableWidget()

# currentItemChanged
