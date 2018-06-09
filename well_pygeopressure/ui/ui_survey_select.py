# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'survey_select.ui'
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

class Ui_surveySelectDialog(object):
    def setupUi(self, surveySelectDialog):
        surveySelectDialog.setObjectName(_fromUtf8("surveySelectDialog"))
        surveySelectDialog.resize(650, 544)
        surveySelectDialog.setModal(True)
        self.surveyButton = QtGui.QPushButton(surveySelectDialog)
        self.surveyButton.setGeometry(QtCore.QRect(20, 10, 120, 23))
        self.surveyButton.setMaximumSize(QtCore.QSize(120, 23))
        self.surveyButton.setFlat(False)
        self.surveyButton.setObjectName(_fromUtf8("surveyButton"))
        self.gridLayoutWidget = QtGui.QWidget(surveySelectDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(310, 50, 321, 271))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.surveyInfoTextEdit = QtGui.QPlainTextEdit(surveySelectDialog)
        self.surveyInfoTextEdit.setGeometry(QtCore.QRect(10, 330, 621, 151))
        self.surveyInfoTextEdit.setReadOnly(True)
        self.surveyInfoTextEdit.setObjectName(_fromUtf8("surveyInfoTextEdit"))
        self.horizontalLayoutWidget = QtGui.QWidget(surveySelectDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 490, 411, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.selectButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.horizontalLayout.addWidget(self.selectButton)
        self.cancelButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.surveyListWidget = QtGui.QListWidget(surveySelectDialog)
        self.surveyListWidget.setGeometry(QtCore.QRect(10, 50, 291, 271))
        self.surveyListWidget.setObjectName(_fromUtf8("surveyListWidget"))
        self.dataRootLabel = QtGui.QLabel(surveySelectDialog)
        self.dataRootLabel.setGeometry(QtCore.QRect(160, 10, 471, 23))
        self.dataRootLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dataRootLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.dataRootLabel.setText(_fromUtf8(""))
        self.dataRootLabel.setObjectName(_fromUtf8("dataRootLabel"))

        self.retranslateUi(surveySelectDialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), surveySelectDialog.close)
        QtCore.QMetaObject.connectSlotsByName(surveySelectDialog)

    def retranslateUi(self, surveySelectDialog):
        surveySelectDialog.setWindowTitle(_translate("surveySelectDialog", "Setup/Select Survey", None))
        self.surveyButton.setText(_translate("surveySelectDialog", "Survey Data Root", None))
        self.selectButton.setText(_translate("surveySelectDialog", "Select", None))
        self.cancelButton.setText(_translate("surveySelectDialog", "Cancel", None))

