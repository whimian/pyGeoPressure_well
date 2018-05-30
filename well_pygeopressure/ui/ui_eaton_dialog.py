# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eaton_dialog.ui'
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

class Ui_eaton_Dialog(object):
    def setupUi(self, eaton_Dialog):
        eaton_Dialog.setObjectName(_fromUtf8("eaton_Dialog"))
        eaton_Dialog.resize(526, 756)
        self.horizontalLayout = QtGui.QHBoxLayout(eaton_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(eaton_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 220, 141, 81))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.predict_Button = QtGui.QPushButton(self.groupBox_3)
        self.predict_Button.setGeometry(QtCore.QRect(60, 50, 65, 23))
        self.predict_Button.setObjectName(_fromUtf8("predict_Button"))
        self.n_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.n_lineEdit.setGeometry(QtCore.QRect(40, 20, 81, 20))
        self.n_lineEdit.setObjectName(_fromUtf8("n_lineEdit"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 21, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 51, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.velocity_comboBox = QtGui.QComboBox(self.groupBox)
        self.velocity_comboBox.setGeometry(QtCore.QRect(10, 70, 121, 22))
        self.velocity_comboBox.setObjectName(_fromUtf8("velocity_comboBox"))
        self.well_comboBox = QtGui.QComboBox(self.groupBox)
        self.well_comboBox.setGeometry(QtCore.QRect(10, 20, 121, 22))
        self.well_comboBox.setObjectName(_fromUtf8("well_comboBox"))
        self.obp_comboBox = QtGui.QComboBox(self.groupBox)
        self.obp_comboBox.setGeometry(QtCore.QRect(10, 110, 121, 22))
        self.obp_comboBox.setObjectName(_fromUtf8("obp_comboBox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.nct_comboBox = QtGui.QComboBox(self.groupBox)
        self.nct_comboBox.setGeometry(QtCore.QRect(10, 150, 121, 22))
        self.nct_comboBox.setObjectName(_fromUtf8("nct_comboBox"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 51, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.n_comboBox = QtGui.QComboBox(self.groupBox)
        self.n_comboBox.setGeometry(QtCore.QRect(10, 190, 121, 22))
        self.n_comboBox.setObjectName(_fromUtf8("n_comboBox"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 51, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 370, 141, 231))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.plot_horizon_Button = QtGui.QPushButton(self.groupBox_4)
        self.plot_horizon_Button.setGeometry(QtCore.QRect(60, 200, 65, 23))
        self.plot_horizon_Button.setObjectName(_fromUtf8("plot_horizon_Button"))
        self.horizon_listWidget = QtGui.QListWidget(self.groupBox_4)
        self.horizon_listWidget.setGeometry(QtCore.QRect(10, 20, 121, 171))
        self.horizon_listWidget.setProperty("isWrapping", True)
        self.horizon_listWidget.setObjectName(_fromUtf8("horizon_listWidget"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 310, 141, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.save_Button = QtGui.QPushButton(self.groupBox_2)
        self.save_Button.setGeometry(QtCore.QRect(120, 20, 20, 20))
        self.save_Button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/save_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_Button.setIcon(icon)
        self.save_Button.setIconSize(QtCore.QSize(20, 20))
        self.save_Button.setFlat(True)
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 121, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(eaton_Dialog)
        QtCore.QMetaObject.connectSlotsByName(eaton_Dialog)

    def retranslateUi(self, eaton_Dialog):
        eaton_Dialog.setWindowTitle(_translate("eaton_Dialog", "PP Eaton", None))
        self.groupBox.setTitle(_translate("eaton_Dialog", "Wells", None))
        self.groupBox_3.setTitle(_translate("eaton_Dialog", "Prediction", None))
        self.predict_Button.setText(_translate("eaton_Dialog", "Predict", None))
        self.n_lineEdit.setText(_translate("eaton_Dialog", "3", None))
        self.label_4.setText(_translate("eaton_Dialog", " N:", None))
        self.label_5.setText(_translate("eaton_Dialog", "Velocity:", None))
        self.label_6.setText(_translate("eaton_Dialog", "OBP:", None))
        self.label_7.setText(_translate("eaton_Dialog", "NCT:", None))
        self.label_8.setText(_translate("eaton_Dialog", "N:", None))
        self.groupBox_4.setTitle(_translate("eaton_Dialog", "Horizons", None))
        self.plot_horizon_Button.setText(_translate("eaton_Dialog", "Plot", None))
        self.groupBox_2.setTitle(_translate("eaton_Dialog", "Save", None))
        self.lineEdit.setText(_translate("eaton_Dialog", "_eaton", None))

import resources_rc
