# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Wed Mar 27 13:51:20 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(945, 458)
        self.namesText = QtWidgets.QTextEdit(Dialog)
        self.namesText.setGeometry(QtCore.QRect(20, 50, 281, 391))
        self.namesText.setObjectName("namesText")
        self.namesTable = QtWidgets.QTableWidget(Dialog)
        self.namesTable.setGeometry(QtCore.QRect(310, 50, 256, 391))
        self.namesTable.setObjectName("namesTable")
        self.namesTable.setColumnCount(0)
        self.namesTable.setRowCount(0)
        self.loginPrefix = QtWidgets.QLineEdit(Dialog)
        self.loginPrefix.setGeometry(QtCore.QRect(320, 20, 113, 22))
        self.loginPrefix.setObjectName("loginPrefix")
        self.adTree = QtWidgets.QTreeWidget(Dialog)
        self.adTree.setGeometry(QtCore.QRect(590, 60, 256, 381))
        self.adTree.setObjectName("adTree")
        self.adTree.headerItem().setText(0, "1")
        self.domainServer = QtWidgets.QLineEdit(Dialog)
        self.domainServer.setGeometry(QtCore.QRect(590, 30, 113, 22))
        self.domainServer.setObjectName("domainServer")
        self.passwordMask = QtWidgets.QLineEdit(Dialog)
        self.passwordMask.setGeometry(QtCore.QRect(450, 20, 113, 22))
        self.passwordMask.setObjectName("passwordMask")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))

