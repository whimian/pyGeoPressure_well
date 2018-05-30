# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format_definition_dialog.ui'
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

class Ui_format_definition_Dialog(object):
    def setupUi(self, format_definition_Dialog):
        format_definition_Dialog.setObjectName(_fromUtf8("format_definition_Dialog"))
        format_definition_Dialog.resize(363, 226)
        self.verticalLayout = QtGui.QVBoxLayout(format_definition_Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(format_definition_Dialog)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(format_definition_Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 160))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 160))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 40, 51, 20))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 61, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.wel_name_spinBox = QtGui.QSpinBox(self.groupBox)
        self.wel_name_spinBox.setGeometry(QtCore.QRect(160, 10, 61, 20))
        self.wel_name_spinBox.setSpecialValueText(_fromUtf8(""))
        self.wel_name_spinBox.setMinimum(1)
        self.wel_name_spinBox.setProperty("value", 1)
        self.wel_name_spinBox.setObjectName(_fromUtf8("wel_name_spinBox"))
        self.x_spinBox = QtGui.QSpinBox(self.groupBox)
        self.x_spinBox.setGeometry(QtCore.QRect(160, 40, 61, 20))
        self.x_spinBox.setMinimum(1)
        self.x_spinBox.setProperty("value", 2)
        self.x_spinBox.setObjectName(_fromUtf8("x_spinBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(90, 40, 61, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.kb_spinBox = QtGui.QSpinBox(self.groupBox)
        self.kb_spinBox.setGeometry(QtCore.QRect(160, 70, 61, 20))
        self.kb_spinBox.setSpecialValueText(_fromUtf8(""))
        self.kb_spinBox.setProperty("value", 4)
        self.kb_spinBox.setObjectName(_fromUtf8("kb_spinBox"))
        self.wd_spinBox = QtGui.QSpinBox(self.groupBox)
        self.wd_spinBox.setGeometry(QtCore.QRect(160, 100, 61, 20))
        self.wd_spinBox.setSpecialValueText(_fromUtf8(""))
        self.wd_spinBox.setObjectName(_fromUtf8("wd_spinBox"))
        self.y_spinBox = QtGui.QSpinBox(self.groupBox)
        self.y_spinBox.setGeometry(QtCore.QRect(230, 40, 61, 20))
        self.y_spinBox.setSpecialValueText(_fromUtf8(""))
        self.y_spinBox.setMinimum(1)
        self.y_spinBox.setProperty("value", 3)
        self.y_spinBox.setObjectName(_fromUtf8("y_spinBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 70, 91, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(60, 100, 91, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.td_spinBox = QtGui.QSpinBox(self.groupBox)
        self.td_spinBox.setGeometry(QtCore.QRect(160, 130, 61, 20))
        self.td_spinBox.setSpecialValueText(_fromUtf8(""))
        self.td_spinBox.setObjectName(_fromUtf8("td_spinBox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(60, 130, 91, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(format_definition_Dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(format_definition_Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), format_definition_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(format_definition_Dialog)

    def retranslateUi(self, format_definition_Dialog):
        format_definition_Dialog.setWindowTitle(_translate("format_definition_Dialog", "Format Definition", None))
        self.label.setText(_translate("format_definition_Dialog", "Specify Necessary Information", None))
        self.comboBox.setItemText(0, _translate("format_definition_Dialog", "X Y", None))
        self.comboBox.setItemText(1, _translate("format_definition_Dialog", "Inl Crl", None))
        self.label_2.setText(_translate("format_definition_Dialog", "Well name", None))
        self.wel_name_spinBox.setPrefix(_translate("format_definition_Dialog", "col: ", None))
        self.x_spinBox.setSpecialValueText(_translate("format_definition_Dialog", "col:", None))
        self.x_spinBox.setPrefix(_translate("format_definition_Dialog", "col: ", None))
        self.label_3.setText(_translate("format_definition_Dialog", "Position", None))
        self.kb_spinBox.setPrefix(_translate("format_definition_Dialog", "col: ", None))
        self.wd_spinBox.setPrefix(_translate("format_definition_Dialog", "col: ", None))
        self.y_spinBox.setPrefix(_translate("format_definition_Dialog", "col: ", None))
        self.label_4.setText(_translate("format_definition_Dialog", "Kelly Bushing (KB)", None))
        self.label_5.setText(_translate("format_definition_Dialog", "Water Depth (WD)", None))
        self.td_spinBox.setPrefix(_translate("format_definition_Dialog", "col: ", None))
        self.label_6.setText(_translate("format_definition_Dialog", "Total Depth (TD)", None))

