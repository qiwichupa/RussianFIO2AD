# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Wed Apr  3 15:20:21 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1023, 633)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridNames = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridNames.setContentsMargins(0, 0, 0, 0)
        self.gridNames.setObjectName("gridNames")
        self.frame_2 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pasteFIO = QtWidgets.QPushButton(self.frame_2)
        self.pasteFIO.setObjectName("pasteFIO")
        self.gridLayout_3.addWidget(self.pasteFIO, 0, 0, 1, 1)
        self.pasteF = QtWidgets.QPushButton(self.frame_2)
        self.pasteF.setObjectName("pasteF")
        self.gridLayout_3.addWidget(self.pasteF, 0, 1, 1, 1)
        self.pasteI = QtWidgets.QPushButton(self.frame_2)
        self.pasteI.setObjectName("pasteI")
        self.gridLayout_3.addWidget(self.pasteI, 0, 2, 1, 1)
        self.pasteO = QtWidgets.QPushButton(self.frame_2)
        self.pasteO.setObjectName("pasteO")
        self.gridLayout_3.addWidget(self.pasteO, 0, 3, 1, 1)
        self.namesTable = QtWidgets.QTableWidget(self.frame_2)
        self.namesTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.namesTable.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.namesTable.setWordWrap(False)
        self.namesTable.setObjectName("namesTable")
        self.namesTable.setColumnCount(3)
        self.namesTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.namesTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.namesTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.namesTable.setHorizontalHeaderItem(2, item)
        self.namesTable.horizontalHeader().setMinimumSectionSize(16)
        self.namesTable.horizontalHeader().setStretchLastSection(True)
        self.namesTable.verticalHeader().setDefaultSectionSize(16)
        self.namesTable.verticalHeader().setMinimumSectionSize(16)
        self.namesTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.namesTable, 1, 0, 1, 4)
        self.gridNames.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLogins = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLogins.setContentsMargins(0, 0, 0, 0)
        self.gridLogins.setObjectName("gridLogins")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.loginsTable = QtWidgets.QTableWidget(self.frame)
        self.loginsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.loginsTable.setWordWrap(False)
        self.loginsTable.setObjectName("loginsTable")
        self.loginsTable.setColumnCount(3)
        self.loginsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.loginsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.loginsTable.setHorizontalHeaderItem(2, item)
        self.loginsTable.horizontalHeader().setMinimumSectionSize(16)
        self.loginsTable.horizontalHeader().setStretchLastSection(True)
        self.loginsTable.verticalHeader().setDefaultSectionSize(16)
        self.loginsTable.verticalHeader().setMinimumSectionSize(16)
        self.gridLayout_2.addWidget(self.loginsTable, 1, 1, 1, 3)
        self.genLogins = QtWidgets.QPushButton(self.frame)
        self.genLogins.setObjectName("genLogins")
        self.gridLayout_2.addWidget(self.genLogins, 2, 1, 1, 1)
        self.copyLogins = QtWidgets.QPushButton(self.frame)
        self.copyLogins.setObjectName("copyLogins")
        self.gridLayout_2.addWidget(self.copyLogins, 2, 3, 1, 1)
        self.loginPrefix = QtWidgets.QLineEdit(self.frame)
        self.loginPrefix.setObjectName("loginPrefix")
        self.gridLayout_2.addWidget(self.loginPrefix, 0, 1, 1, 1)
        self.passwordMask = QtWidgets.QLineEdit(self.frame)
        self.passwordMask.setObjectName("passwordMask")
        self.gridLayout_2.addWidget(self.passwordMask, 0, 3, 1, 1)
        self.loginTemplate = QtWidgets.QLineEdit(self.frame)
        self.loginTemplate.setPlaceholderText("")
        self.loginTemplate.setObjectName("loginTemplate")
        self.gridLayout_2.addWidget(self.loginTemplate, 0, 2, 1, 1)
        self.gridLogins.addWidget(self.frame, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridAD = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridAD.setContentsMargins(0, 0, 0, 0)
        self.gridAD.setObjectName("gridAD")
        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.adTree = QtWidgets.QTreeWidget(self.frame_3)
        self.adTree.setObjectName("adTree")
        self.adTree.headerItem().setText(0, "Выбери OU")
        self.gridLayout_4.addWidget(self.adTree, 1, 1, 1, 1)
        self.createAccounts = QtWidgets.QPushButton(self.frame_3)
        self.createAccounts.setEnabled(False)
        self.createAccounts.setObjectName("createAccounts")
        self.gridLayout_4.addWidget(self.createAccounts, 0, 1, 1, 1)
        self.gridAD.addWidget(self.frame_3, 0, 0, 1, 1)
        self.logBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget_3)
        self.logBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.logBrowser.setObjectName("logBrowser")
        self.gridAD.addWidget(self.logBrowser, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.pasteFIO.setText(QtWidgets.QApplication.translate("Dialog", "Вставить ФИО", None, -1))
        self.pasteF.setText(QtWidgets.QApplication.translate("Dialog", "Только Ф", None, -1))
        self.pasteI.setText(QtWidgets.QApplication.translate("Dialog", "Только И", None, -1))
        self.pasteO.setText(QtWidgets.QApplication.translate("Dialog", "Только О", None, -1))
        self.namesTable.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Dialog", "Фамилия", None, -1))
        self.namesTable.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Dialog", "Имя", None, -1))
        self.namesTable.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Dialog", "Отчество", None, -1))
        self.loginsTable.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("Dialog", "DisplayName", None, -1))
        self.loginsTable.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("Dialog", "Login", None, -1))
        self.loginsTable.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("Dialog", "Password", None, -1))
        self.genLogins.setText(QtWidgets.QApplication.translate("Dialog", "Генерировать", None, -1))
        self.copyLogins.setText(QtWidgets.QApplication.translate("Dialog", "Скопировать всё", None, -1))
        self.loginPrefix.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "Префикс логина", None, -1))
        self.passwordMask.setToolTip(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p>! - БОЛЬШАЯ БУКВА<br/>@ - маленькая буква<br/># - цифра<br/>$ - знак пунктуации<br/><br/>Например:<br/>!@###$### - Rd834)214</p></body></html>", None, -1))
        self.passwordMask.setText(QtWidgets.QApplication.translate("Dialog", "!@######", None, -1))
        self.loginTemplate.setToolTip(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">f</span> - фамилия<br/><span style=\" font-weight:600;\">i</span> - имя<br/><span style=\" font-weight:600;\">o</span> - отчество<br/><br/>Используйте цифры, например:<br/><span style=\" font-weight:600;\">i2</span> - две первых буквы имени (транслитерированного)<br/><br/><span style=\" font-weight:600;\">f_i1o1</span> - Ivanov_II</p></body></html>", None, -1))
        self.loginTemplate.setText(QtWidgets.QApplication.translate("Dialog", "f_i1o1", None, -1))
        self.createAccounts.setText(QtWidgets.QApplication.translate("Dialog", "Создать аккаунты в:", None, -1))

