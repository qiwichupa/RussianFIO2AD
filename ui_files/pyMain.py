# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Tue Apr  2 10:59:21 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1023, 553)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.pasteFIO = QtWidgets.QPushButton(Dialog)
        self.pasteFIO.setObjectName("pasteFIO")
        self.gridLayout.addWidget(self.pasteFIO, 0, 0, 1, 1)
        self.pasteF = QtWidgets.QPushButton(Dialog)
        self.pasteF.setObjectName("pasteF")
        self.gridLayout.addWidget(self.pasteF, 0, 1, 1, 1)
        self.pasteI = QtWidgets.QPushButton(Dialog)
        self.pasteI.setObjectName("pasteI")
        self.gridLayout.addWidget(self.pasteI, 0, 2, 1, 1)
        self.pasteO = QtWidgets.QPushButton(Dialog)
        self.pasteO.setObjectName("pasteO")
        self.gridLayout.addWidget(self.pasteO, 0, 3, 1, 1)
        self.loginPrefix = QtWidgets.QLineEdit(Dialog)
        self.loginPrefix.setObjectName("loginPrefix")
        self.gridLayout.addWidget(self.loginPrefix, 0, 4, 1, 1)
        self.passwordMask = QtWidgets.QLineEdit(Dialog)
        self.passwordMask.setObjectName("passwordMask")
        self.gridLayout.addWidget(self.passwordMask, 0, 5, 1, 1)
        self.domainServer = QtWidgets.QLineEdit(Dialog)
        self.domainServer.setObjectName("domainServer")
        self.gridLayout.addWidget(self.domainServer, 0, 6, 1, 1)
        self.namesTable = QtWidgets.QTableWidget(Dialog)
        self.namesTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.namesTable.setObjectName("namesTable")
        self.namesTable.setColumnCount(3)
        self.namesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.namesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.namesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.namesTable.setHorizontalHeaderItem(2, item)
        self.namesTable.horizontalHeader().setStretchLastSection(True)
        self.namesTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.namesTable, 1, 0, 1, 4)
        self.loginsTable = QtWidgets.QTableWidget(Dialog)
        self.loginsTable.setObjectName("loginsTable")
        self.loginsTable.setColumnCount(3)
        self.loginsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.loginsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginsTable.setHorizontalHeaderItem(2, item)
        self.gridLayout.addWidget(self.loginsTable, 1, 4, 1, 2)
        self.adTree = QtWidgets.QTreeWidget(Dialog)
        self.adTree.setObjectName("adTree")
        self.adTree.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.adTree, 1, 6, 1, 1)
        self.genLogins = QtWidgets.QPushButton(Dialog)
        self.genLogins.setObjectName("genLogins")
        self.gridLayout.addWidget(self.genLogins, 2, 4, 1, 2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 6)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pasteFIO.setText(QtWidgets.QApplication.translate("Dialog", "Paste All", None, -1))
        self.pasteF.setText(QtWidgets.QApplication.translate("Dialog", "P.F", None, -1))
        self.pasteI.setText(QtWidgets.QApplication.translate("Dialog", "P.I", None, -1))
        self.pasteO.setText(QtWidgets.QApplication.translate("Dialog", "P.O", None, -1))
        self.namesTable.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Dialog", "F", None, -1))
        self.namesTable.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Dialog", "I", None, -1))
        self.namesTable.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Dialog", "O", None, -1))
        self.loginsTable.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Dialog", "DisplayName", None, -1))
        self.loginsTable.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Dialog", "Login", None, -1))
        self.loginsTable.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Dialog", "Pass", None, -1))
        self.genLogins.setText(QtWidgets.QApplication.translate("Dialog", "Generate Logins", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "TextLabel", None, -1))

