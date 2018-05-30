# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'discern_shale_dialog.ui'
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

class Ui_discern_shale_Dialog(object):
    def setupUi(self, discern_shale_Dialog):
        discern_shale_Dialog.setObjectName(_fromUtf8("discern_shale_Dialog"))
        discern_shale_Dialog.resize(644, 752)
        self.horizontalLayout = QtGui.QHBoxLayout(discern_shale_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(discern_shale_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 20, 31, 20))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.well_comboBox = QtGui.QComboBox(self.groupBox)
        self.well_comboBox.setGeometry(QtCore.QRect(40, 20, 81, 20))
        self.well_comboBox.setObjectName(_fromUtf8("well_comboBox"))
        self.log_comboBox = QtGui.QComboBox(self.groupBox)
        self.log_comboBox.setGeometry(QtCore.QRect(10, 70, 111, 20))
        self.log_comboBox.setObjectName(_fromUtf8("log_comboBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 31, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sh_log_comboBox = QtGui.QComboBox(self.groupBox)
        self.sh_log_comboBox.setGeometry(QtCore.QRect(10, 120, 111, 20))
        self.sh_log_comboBox.setObjectName(_fromUtf8("sh_log_comboBox"))
        self.shale_checkBox = QtGui.QCheckBox(self.groupBox)
        self.shale_checkBox.setGeometry(QtCore.QRect(10, 100, 91, 17))
        self.shale_checkBox.setObjectName(_fromUtf8("shale_checkBox"))
        self.plot_Button = QtGui.QPushButton(self.groupBox)
        self.plot_Button.setGeometry(QtCore.QRect(60, 180, 65, 23))
        self.plot_Button.setObjectName(_fromUtf8("plot_Button"))
        self.thresh_spinBox = QtGui.QSpinBox(self.groupBox)
        self.thresh_spinBox.setGeometry(QtCore.QRect(60, 150, 61, 22))
        self.thresh_spinBox.setMaximum(100)
        self.thresh_spinBox.setProperty("value", 35)
        self.thresh_spinBox.setObjectName(_fromUtf8("thresh_spinBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 41, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 270, 141, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plot_horizon_Button = QtGui.QPushButton(self.groupBox_2)
        self.plot_horizon_Button.setGeometry(QtCore.QRect(60, 200, 65, 23))
        self.plot_horizon_Button.setObjectName(_fromUtf8("plot_horizon_Button"))
        self.horizon_listWidget = QtGui.QListWidget(self.groupBox_2)
        self.horizon_listWidget.setGeometry(QtCore.QRect(10, 20, 121, 171))
        self.horizon_listWidget.setProperty("isWrapping", True)
        self.horizon_listWidget.setObjectName(_fromUtf8("horizon_listWidget"))
        self.plot_horizon_Button.raise_()
        self.horizon_listWidget.raise_()
        self.plot_horizon_Button.raise_()
        self.horizon_listWidget.raise_()
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 210, 111, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.save_Button = QtGui.QPushButton(self.groupBox)
        self.save_Button.setGeometry(QtCore.QRect(60, 240, 65, 23))
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(discern_shale_Dialog)
        QtCore.QMetaObject.connectSlotsByName(discern_shale_Dialog)

    def retranslateUi(self, discern_shale_Dialog):
        discern_shale_Dialog.setWindowTitle(_translate("discern_shale_Dialog", "Discern Shale Dialog", None))
        self.groupBox.setTitle(_translate("discern_shale_Dialog", "Data", None))
        self.label.setText(_translate("discern_shale_Dialog", "Well", None))
        self.label_2.setText(_translate("discern_shale_Dialog", "Log", None))
        self.shale_checkBox.setText(_translate("discern_shale_Dialog", "Shale Volume", None))
        self.plot_Button.setText(_translate("discern_shale_Dialog", "Plot", None))
        self.thresh_spinBox.setSuffix(_translate("discern_shale_Dialog", "%", None))
        self.label_3.setText(_translate("discern_shale_Dialog", "Thresh", None))
        self.groupBox_2.setTitle(_translate("discern_shale_Dialog", "Horizons", None))
        self.plot_horizon_Button.setText(_translate("discern_shale_Dialog", "Plot", None))
        self.lineEdit.setText(_translate("discern_shale_Dialog", "sh_", None))
        self.save_Button.setText(_translate("discern_shale_Dialog", "Save", None))

