# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_multiple_wells_from_file_dialog.ui'
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

class Ui_read_multiple_wells_from_file_Dialog(object):
    def setupUi(self, read_multiple_wells_from_file_Dialog):
        read_multiple_wells_from_file_Dialog.setObjectName(_fromUtf8("read_multiple_wells_from_file_Dialog"))
        read_multiple_wells_from_file_Dialog.resize(568, 173)
        read_multiple_wells_from_file_Dialog.setMaximumSize(QtCore.QSize(628, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(read_multiple_wells_from_file_Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(read_multiple_wells_from_file_Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.groupBox = QtGui.QGroupBox(read_multiple_wells_from_file_Dialog)
        self.groupBox.setMinimumSize(QtCore.QSize(550, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(550, 100))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.examineButton = QtGui.QPushButton(self.groupBox)
        self.examineButton.setGeometry(QtCore.QRect(470, 10, 75, 23))
        self.examineButton.setObjectName(_fromUtf8("examineButton"))
        self.selectButton = QtGui.QPushButton(self.groupBox)
        self.selectButton.setGeometry(QtCore.QRect(390, 10, 75, 23))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 129, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.file_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.file_lineEdit.setGeometry(QtCore.QRect(130, 12, 250, 20))
        self.file_lineEdit.setMinimumSize(QtCore.QSize(250, 20))
        self.file_lineEdit.setMaximumSize(QtCore.QSize(300, 20))
        self.file_lineEdit.setReadOnly(True)
        self.file_lineEdit.setObjectName(_fromUtf8("file_lineEdit"))
        self.header_size_spinBox = QtGui.QSpinBox(self.groupBox)
        self.header_size_spinBox.setGeometry(QtCore.QRect(130, 40, 100, 20))
        self.header_size_spinBox.setMinimumSize(QtCore.QSize(100, 20))
        self.header_size_spinBox.setMaximumSize(QtCore.QSize(100, 20))
        self.header_size_spinBox.setProperty("value", 1)
        self.header_size_spinBox.setObjectName(_fromUtf8("header_size_spinBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 40, 74, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(-70, 70, 191, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.format_lineEdit = QtGui.QLineEdit(self.groupBox)
        self.format_lineEdit.setGeometry(QtCore.QRect(130, 70, 100, 20))
        self.format_lineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.format_lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.format_lineEdit.setReadOnly(True)
        self.format_lineEdit.setObjectName(_fromUtf8("format_lineEdit"))
        self.defineButton = QtGui.QPushButton(self.groupBox)
        self.defineButton.setGeometry(QtCore.QRect(240, 70, 80, 23))
        self.defineButton.setObjectName(_fromUtf8("defineButton"))
        self.verticalLayout.addWidget(self.groupBox)
        self.buttonBox = QtGui.QDialogButtonBox(read_multiple_wells_from_file_Dialog)
        self.buttonBox.setMaximumSize(QtCore.QSize(610, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(read_multiple_wells_from_file_Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), read_multiple_wells_from_file_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(read_multiple_wells_from_file_Dialog)

    def retranslateUi(self, read_multiple_wells_from_file_Dialog):
        read_multiple_wells_from_file_Dialog.setWindowTitle(_translate("read_multiple_wells_from_file_Dialog", "Multiple Wells", None))
        self.label.setText(_translate("read_multiple_wells_from_file_Dialog", "Create multiple wells", None))
        self.examineButton.setText(_translate("read_multiple_wells_from_file_Dialog", "Examine", None))
        self.selectButton.setText(_translate("read_multiple_wells_from_file_Dialog", "Select", None))
        self.label_2.setText(_translate("read_multiple_wells_from_file_Dialog", "Input file", None))
        self.label_3.setText(_translate("read_multiple_wells_from_file_Dialog", "File header size", None))
        self.label_4.setText(_translate("read_multiple_wells_from_file_Dialog", "Format definition", None))
        self.format_lineEdit.setText(_translate("read_multiple_wells_from_file_Dialog", "<incomplete>", None))
        self.defineButton.setText(_translate("read_multiple_wells_from_file_Dialog", "Define", None))

