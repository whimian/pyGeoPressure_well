# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'well_marker_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_well_marker_Dialog(object):
    def setupUi(self, well_marker_Dialog):
        well_marker_Dialog.setObjectName(_fromUtf8("well_marker_Dialog"))
        well_marker_Dialog.resize(568, 411)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/layer_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        well_marker_Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(well_marker_Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(well_marker_Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newButton = QtGui.QPushButton(well_marker_Dialog)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.horizontalLayout.addWidget(self.newButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.saveButton = QtGui.QPushButton(well_marker_Dialog)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.cancelButton = QtGui.QPushButton(well_marker_Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(well_marker_Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), well_marker_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(well_marker_Dialog)

    def retranslateUi(self, well_marker_Dialog):
        well_marker_Dialog.setWindowTitle(_translate("well_marker_Dialog", "Edit Markers", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("well_marker_Dialog", "Name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("well_marker_Dialog", "TVD (m)", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("well_marker_Dialog", "TVDSS (m)", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("well_marker_Dialog", "Color", None))
        self.newButton.setText(_translate("well_marker_Dialog", "New", None))
        self.saveButton.setText(_translate("well_marker_Dialog", "Save", None))
        self.cancelButton.setText(_translate("well_marker_Dialog", "Cancel", None))

import resources_rc
