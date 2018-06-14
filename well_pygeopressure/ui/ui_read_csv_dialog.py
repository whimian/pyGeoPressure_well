# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'read_csv_dialog.ui'
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

class Ui_read_csv_Dialog(object):
    def setupUi(self, read_csv_Dialog):
        read_csv_Dialog.setObjectName(_fromUtf8("read_csv_Dialog"))
        read_csv_Dialog.resize(533, 151)
        read_csv_Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/import_icon")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        read_csv_Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(read_csv_Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(read_csv_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMaximumSize(QtCore.QSize(16777215, 23))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 0, 1, 7)
        self.examineButton = QtGui.QPushButton(read_csv_Dialog)
        self.examineButton.setObjectName(_fromUtf8("examineButton"))
        self.gridLayout.addWidget(self.examineButton, 1, 6, 1, 1)
        self.selectButton = QtGui.QPushButton(read_csv_Dialog)
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.gridLayout.addWidget(self.selectButton, 1, 5, 1, 1)
        self.file_lineEdit = QtGui.QLineEdit(read_csv_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.file_lineEdit.sizePolicy().hasHeightForWidth())
        self.file_lineEdit.setSizePolicy(sizePolicy)
        self.file_lineEdit.setMinimumSize(QtCore.QSize(250, 20))
        self.file_lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.file_lineEdit.setSizeIncrement(QtCore.QSize(0, 0))
        self.file_lineEdit.setReadOnly(True)
        self.file_lineEdit.setObjectName(_fromUtf8("file_lineEdit"))
        self.gridLayout.addWidget(self.file_lineEdit, 1, 2, 1, 3)
        self.defineButton = QtGui.QPushButton(read_csv_Dialog)
        self.defineButton.setObjectName(_fromUtf8("defineButton"))
        self.gridLayout.addWidget(self.defineButton, 3, 4, 1, 1)
        self.label = QtGui.QLabel(read_csv_Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 6)
        self.label_4 = QtGui.QLabel(read_csv_Dialog)
        self.label_4.setMinimumSize(QtCore.QSize(91, 0))
        self.label_4.setMaximumSize(QtCore.QSize(91, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.header_size_spinBox = QtGui.QSpinBox(read_csv_Dialog)
        self.header_size_spinBox.setMinimumSize(QtCore.QSize(100, 20))
        self.header_size_spinBox.setMaximumSize(QtCore.QSize(100, 20))
        self.header_size_spinBox.setProperty("value", 1)
        self.header_size_spinBox.setObjectName(_fromUtf8("header_size_spinBox"))
        self.gridLayout.addWidget(self.header_size_spinBox, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(read_csv_Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(91, 0))
        self.label_2.setMaximumSize(QtCore.QSize(91, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.format_lineEdit = QtGui.QLineEdit(read_csv_Dialog)
        self.format_lineEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.format_lineEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.format_lineEdit.setReadOnly(True)
        self.format_lineEdit.setObjectName(_fromUtf8("format_lineEdit"))
        self.gridLayout.addWidget(self.format_lineEdit, 3, 2, 1, 1)
        self.label_3 = QtGui.QLabel(read_csv_Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(91, 0))
        self.label_3.setMaximumSize(QtCore.QSize(91, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 3, 1, 1)

        self.retranslateUi(read_csv_Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), read_csv_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(read_csv_Dialog)

    def retranslateUi(self, read_csv_Dialog):
        read_csv_Dialog.setWindowTitle(_translate("read_csv_Dialog", "Read CSV", None))
        self.examineButton.setText(_translate("read_csv_Dialog", "Examine", None))
        self.selectButton.setText(_translate("read_csv_Dialog", "Select", None))
        self.defineButton.setText(_translate("read_csv_Dialog", "Define", None))
        self.label.setText(_translate("read_csv_Dialog", "Create multiple wells", None))
        self.label_4.setText(_translate("read_csv_Dialog", "Format definition", None))
        self.label_2.setText(_translate("read_csv_Dialog", "Input file", None))
        self.format_lineEdit.setText(_translate("read_csv_Dialog", "<incomplete>", None))
        self.label_3.setText(_translate("read_csv_Dialog", "File header size", None))

import resources_rc
