# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimize_eaton_dialog.ui'
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

class Ui_optimize_eaton_Dialog(object):
    def setupUi(self, optimize_eaton_Dialog):
        optimize_eaton_Dialog.setObjectName(_fromUtf8("optimize_eaton_Dialog"))
        optimize_eaton_Dialog.resize(844, 601)
        self.horizontalLayout = QtGui.QHBoxLayout(optimize_eaton_Dialog)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(optimize_eaton_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.well_listWidget = QtGui.QListWidget(self.groupBox)
        self.well_listWidget.setGeometry(QtCore.QRect(0, 20, 131, 151))
        self.well_listWidget.setObjectName(_fromUtf8("well_listWidget"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 51, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.velocity_comboBox = QtGui.QComboBox(self.groupBox)
        self.velocity_comboBox.setGeometry(QtCore.QRect(10, 190, 121, 22))
        self.velocity_comboBox.setObjectName(_fromUtf8("velocity_comboBox"))
        self.nct_comboBox = QtGui.QComboBox(self.groupBox)
        self.nct_comboBox.setGeometry(QtCore.QRect(10, 270, 121, 22))
        self.nct_comboBox.setObjectName(_fromUtf8("nct_comboBox"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 51, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 51, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.obp_comboBox = QtGui.QComboBox(self.groupBox)
        self.obp_comboBox.setGeometry(QtCore.QRect(10, 230, 121, 22))
        self.obp_comboBox.setObjectName(_fromUtf8("obp_comboBox"))
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_4 = QtGui.QGroupBox(optimize_eaton_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(140, 0))
        self.groupBox_4.setMaximumSize(QtCore.QSize(140, 16777215))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 140, 141, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.save_Button = QtGui.QPushButton(self.groupBox_2)
        self.save_Button.setGeometry(QtCore.QRect(60, 50, 65, 23))
        self.save_Button.setObjectName(_fromUtf8("save_Button"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(40, 100, 41, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.max_lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.max_lineEdit.setGeometry(QtCore.QRect(80, 40, 51, 20))
        self.max_lineEdit.setObjectName(_fromUtf8("max_lineEdit"))
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 51, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(60, 40, 16, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.contour_Button = QtGui.QPushButton(self.groupBox_4)
        self.contour_Button.setGeometry(QtCore.QRect(60, 70, 65, 23))
        self.contour_Button.setObjectName(_fromUtf8("contour_Button"))
        self.min_lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.min_lineEdit.setGeometry(QtCore.QRect(0, 40, 51, 20))
        self.min_lineEdit.setObjectName(_fromUtf8("min_lineEdit"))
        self.n_lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.n_lineEdit.setGeometry(QtCore.QRect(80, 100, 51, 20))
        self.n_lineEdit.setObjectName(_fromUtf8("n_lineEdit"))
        self.horizontalLayout.addWidget(self.groupBox_4)

        self.retranslateUi(optimize_eaton_Dialog)
        QtCore.QMetaObject.connectSlotsByName(optimize_eaton_Dialog)

    def retranslateUi(self, optimize_eaton_Dialog):
        optimize_eaton_Dialog.setWindowTitle(_translate("optimize_eaton_Dialog", "Optimize Eaton", None))
        self.groupBox.setTitle(_translate("optimize_eaton_Dialog", "Wells", None))
        self.label_5.setText(_translate("optimize_eaton_Dialog", "Velocity:", None))
        self.label_7.setText(_translate("optimize_eaton_Dialog", "NCT:", None))
        self.label_6.setText(_translate("optimize_eaton_Dialog", "OBP:", None))
        self.groupBox_4.setTitle(_translate("optimize_eaton_Dialog", "Optimize", None))
        self.groupBox_2.setTitle(_translate("optimize_eaton_Dialog", "Save", None))
        self.save_Button.setText(_translate("optimize_eaton_Dialog", "Save", None))
        self.lineEdit.setText(_translate("optimize_eaton_Dialog", "N", None))
        self.label_11.setText(_translate("optimize_eaton_Dialog", "best N:", None))
        self.max_lineEdit.setText(_translate("optimize_eaton_Dialog", "4", None))
        self.label_10.setText(_translate("optimize_eaton_Dialog", "N range:", None))
        self.label_9.setText(_translate("optimize_eaton_Dialog", "---", None))
        self.contour_Button.setText(_translate("optimize_eaton_Dialog", "contour", None))
        self.min_lineEdit.setText(_translate("optimize_eaton_Dialog", "2", None))
        self.n_lineEdit.setText(_translate("optimize_eaton_Dialog", "1500", None))

