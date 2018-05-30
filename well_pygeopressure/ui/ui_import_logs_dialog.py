# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_logs_dialog.ui'
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

class Ui_import_logs_Dialog(object):
    def setupUi(self, import_logs_Dialog):
        import_logs_Dialog.setObjectName(_fromUtf8("import_logs_Dialog"))
        import_logs_Dialog.resize(540, 310)
        import_logs_Dialog.setMinimumSize(QtCore.QSize(540, 310))
        import_logs_Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLayout = QtGui.QGridLayout(import_logs_Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.file_lineEdit = QtGui.QLineEdit(import_logs_Dialog)
        self.file_lineEdit.setMinimumSize(QtCore.QSize(250, 23))
        self.file_lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.file_lineEdit.setReadOnly(True)
        self.file_lineEdit.setObjectName(_fromUtf8("file_lineEdit"))
        self.gridLayout.addWidget(self.file_lineEdit, 0, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(import_logs_Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 4)
        self.label_4 = QtGui.QLabel(import_logs_Dialog)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.wells_comboBox = QtGui.QComboBox(import_logs_Dialog)
        self.wells_comboBox.setObjectName(_fromUtf8("wells_comboBox"))
        self.gridLayout.addWidget(self.wells_comboBox, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(import_logs_Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.undefined_lineEdit = QtGui.QLineEdit(import_logs_Dialog)
        self.undefined_lineEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.undefined_lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.undefined_lineEdit.setReadOnly(True)
        self.undefined_lineEdit.setObjectName(_fromUtf8("undefined_lineEdit"))
        self.gridLayout.addWidget(self.undefined_lineEdit, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(import_logs_Dialog)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.importButton = QtGui.QPushButton(import_logs_Dialog)
        self.importButton.setMaximumSize(QtCore.QSize(62, 16777215))
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.gridLayout.addWidget(self.importButton, 4, 2, 1, 1)
        self.selectButton = QtGui.QPushButton(import_logs_Dialog)
        self.selectButton.setMaximumSize(QtCore.QSize(62, 16777215))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.gridLayout.addWidget(self.selectButton, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.cancelButton = QtGui.QPushButton(import_logs_Dialog)
        self.cancelButton.setMaximumSize(QtCore.QSize(62, 16777215))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 4, 3, 1, 1)

        self.retranslateUi(import_logs_Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), import_logs_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(import_logs_Dialog)

    def retranslateUi(self, import_logs_Dialog):
        import_logs_Dialog.setWindowTitle(_translate("import_logs_Dialog", "Import Logs", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("import_logs_Dialog", "Description", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("import_logs_Dialog", "Unit", None))
        self.label_4.setText(_translate("import_logs_Dialog", "Add to Well", None))
        self.label_2.setText(_translate("import_logs_Dialog", "Input file", None))
        self.undefined_lineEdit.setText(_translate("import_logs_Dialog", "-999.25", None))
        self.label_3.setText(_translate("import_logs_Dialog", "Undefined value in logs", None))
        self.importButton.setText(_translate("import_logs_Dialog", "Import", None))
        self.selectButton.setText(_translate("import_logs_Dialog", "Select", None))
        self.cancelButton.setText(_translate("import_logs_Dialog", "Cancel", None))

