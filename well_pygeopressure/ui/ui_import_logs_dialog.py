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
        import_logs_Dialog.setMaximumSize(QtCore.QSize(540, 310))
        self.selectButton = QtGui.QPushButton(import_logs_Dialog)
        self.selectButton.setGeometry(QtCore.QRect(410, 20, 75, 20))
        self.selectButton.setObjectName(_fromUtf8("selectButton"))
        self.label_2 = QtGui.QLabel(import_logs_Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 129, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.file_lineEdit = QtGui.QLineEdit(import_logs_Dialog)
        self.file_lineEdit.setGeometry(QtCore.QRect(150, 20, 250, 20))
        self.file_lineEdit.setMinimumSize(QtCore.QSize(250, 20))
        self.file_lineEdit.setMaximumSize(QtCore.QSize(300, 20))
        self.file_lineEdit.setReadOnly(True)
        self.file_lineEdit.setObjectName(_fromUtf8("file_lineEdit"))
        self.label_3 = QtGui.QLabel(import_logs_Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 129, 20))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.undefined_lineEdit = QtGui.QLineEdit(import_logs_Dialog)
        self.undefined_lineEdit.setGeometry(QtCore.QRect(150, 50, 100, 20))
        self.undefined_lineEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.undefined_lineEdit.setMaximumSize(QtCore.QSize(100, 20))
        self.undefined_lineEdit.setReadOnly(True)
        self.undefined_lineEdit.setObjectName(_fromUtf8("undefined_lineEdit"))
        self.label_4 = QtGui.QLabel(import_logs_Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 280, 129, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.wells_comboBox = QtGui.QComboBox(import_logs_Dialog)
        self.wells_comboBox.setGeometry(QtCore.QRect(160, 280, 201, 20))
        self.wells_comboBox.setObjectName(_fromUtf8("wells_comboBox"))
        self.tableWidget = QtGui.QTableWidget(import_logs_Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 521, 192))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.retranslateUi(import_logs_Dialog)
        QtCore.QMetaObject.connectSlotsByName(import_logs_Dialog)

    def retranslateUi(self, import_logs_Dialog):
        import_logs_Dialog.setWindowTitle(_translate("import_logs_Dialog", "Import Logs", None))
        self.selectButton.setText(_translate("import_logs_Dialog", "Select", None))
        self.label_2.setText(_translate("import_logs_Dialog", "Input file", None))
        self.label_3.setText(_translate("import_logs_Dialog", "Undefined value in logs", None))
        self.undefined_lineEdit.setText(_translate("import_logs_Dialog", "-999.25", None))
        self.label_4.setText(_translate("import_logs_Dialog", "Add to Well", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("import_logs_Dialog", "Curve", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("import_logs_Dialog", "Unit", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("import_logs_Dialog", "Description", None))

