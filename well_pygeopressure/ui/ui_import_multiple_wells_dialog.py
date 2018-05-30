# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_multiple_wells_dialog.ui'
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

class Ui_import_multiple_wells_Dialog(object):
    def setupUi(self, import_multiple_wells_Dialog):
        import_multiple_wells_Dialog.setObjectName(_fromUtf8("import_multiple_wells_Dialog"))
        import_multiple_wells_Dialog.resize(704, 413)
        self.gridLayout = QtGui.QGridLayout(import_multiple_wells_Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(import_multiple_wells_Dialog)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.openButton = QtGui.QPushButton(import_multiple_wells_Dialog)
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.horizontalLayout.addWidget(self.openButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.createButton = QtGui.QPushButton(import_multiple_wells_Dialog)
        self.createButton.setObjectName(_fromUtf8("createButton"))
        self.horizontalLayout.addWidget(self.createButton)
        self.cancelButton = QtGui.QPushButton(import_multiple_wells_Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(import_multiple_wells_Dialog)
        QtCore.QObject.connect(self.cancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), import_multiple_wells_Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(import_multiple_wells_Dialog)

    def retranslateUi(self, import_multiple_wells_Dialog):
        import_multiple_wells_Dialog.setWindowTitle(_translate("import_multiple_wells_Dialog", "Multiple Wells", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("import_multiple_wells_Dialog", "Well name", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("import_multiple_wells_Dialog", "X (m)", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("import_multiple_wells_Dialog", "Y (m)", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("import_multiple_wells_Dialog", "KB (m)", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("import_multiple_wells_Dialog", "WD (m)", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("import_multiple_wells_Dialog", "TD (m)", None))
        self.openButton.setText(_translate("import_multiple_wells_Dialog", "Open File", None))
        self.createButton.setText(_translate("import_multiple_wells_Dialog", "Create", None))
        self.cancelButton.setText(_translate("import_multiple_wells_Dialog", "Cancel", None))

