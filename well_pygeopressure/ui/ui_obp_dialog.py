# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obp_dialog.ui'
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

class Ui_obp_Dialog(object):
    def setupUi(self, obp_Dialog):
        obp_Dialog.setObjectName(_fromUtf8("obp_Dialog"))
        obp_Dialog.resize(647, 754)
        self.horizontalLayout = QtGui.QHBoxLayout(obp_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(obp_Dialog)
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
        self.label_2.setGeometry(QtCore.QRect(0, 50, 41, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 310, 141, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plot_horizon_Button = QtGui.QPushButton(self.groupBox_2)
        self.plot_horizon_Button.setGeometry(QtCore.QRect(60, 200, 65, 23))
        self.plot_horizon_Button.setObjectName(_fromUtf8("plot_horizon_Button"))
        self.horizon_listWidget = QtGui.QListWidget(self.groupBox_2)
        self.horizon_listWidget.setGeometry(QtCore.QRect(10, 20, 121, 171))
        self.horizon_listWidget.setProperty("isWrapping", True)
        self.horizon_listWidget.setObjectName(_fromUtf8("horizon_listWidget"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 250, 111, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.save_Button = QtGui.QPushButton(self.groupBox)
        self.save_Button.setGeometry(QtCore.QRect(60, 280, 65, 23))
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 100, 141, 141))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.obp_Button = QtGui.QPushButton(self.groupBox_3)
        self.obp_Button.setGeometry(QtCore.QRect(60, 110, 65, 23))
        self.obp_Button.setObjectName(_fromUtf8("obp_Button"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 31, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.kb_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.kb_lineEdit.setGeometry(QtCore.QRect(50, 20, 71, 20))
        self.kb_lineEdit.setObjectName(_fromUtf8("kb_lineEdit"))
        self.wd_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.wd_lineEdit.setGeometry(QtCore.QRect(50, 50, 71, 20))
        self.wd_lineEdit.setObjectName(_fromUtf8("wd_lineEdit"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 31, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.rho_lineEdit = QtGui.QLineEdit(self.groupBox_3)
        self.rho_lineEdit.setGeometry(QtCore.QRect(70, 80, 51, 20))
        self.rho_lineEdit.setObjectName(_fromUtf8("rho_lineEdit"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(0, 80, 61, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.groupBox)

        self.retranslateUi(obp_Dialog)
        QtCore.QMetaObject.connectSlotsByName(obp_Dialog)

    def retranslateUi(self, obp_Dialog):
        obp_Dialog.setWindowTitle(_translate("obp_Dialog", "Overburden Pressure", None))
        self.groupBox.setTitle(_translate("obp_Dialog", "Data", None))
        self.label.setText(_translate("obp_Dialog", "Well", None))
        self.label_2.setText(_translate("obp_Dialog", "Denstiy", None))
        self.groupBox_2.setTitle(_translate("obp_Dialog", "Horizons", None))
        self.plot_horizon_Button.setText(_translate("obp_Dialog", "Plot", None))
        self.lineEdit.setText(_translate("obp_Dialog", "OBP", None))
        self.save_Button.setText(_translate("obp_Dialog", "Save", None))
        self.groupBox_3.setTitle(_translate("obp_Dialog", "OBP", None))
        self.obp_Button.setText(_translate("obp_Dialog", "OBP", None))
        self.label_4.setText(_translate("obp_Dialog", "KB", None))
        self.kb_lineEdit.setText(_translate("obp_Dialog", "1500", None))
        self.wd_lineEdit.setText(_translate("obp_Dialog", "1500", None))
        self.label_5.setText(_translate("obp_Dialog", "WD", None))
        self.rho_lineEdit.setText(_translate("obp_Dialog", "1.01", None))
        self.label_6.setText(_translate("obp_Dialog", "Rho Water ", None))

