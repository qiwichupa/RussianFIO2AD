# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Fri Jun 12 20:25:59 2020
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1054, 517)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/main.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridNames = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridNames.setSpacing(1)
        self.gridNames.setContentsMargins(0, 0, 0, 0)
        self.gridNames.setObjectName("gridNames")
        self.frame_2 = QtWidgets.QFrame(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonPasteFIO = QtWidgets.QPushButton(self.frame_2)
        self.buttonPasteFIO.setToolTip("")
        self.buttonPasteFIO.setObjectName("buttonPasteFIO")
        self.gridLayout_3.addWidget(self.buttonPasteFIO, 0, 0, 1, 1)
        self.buttonPasteF = QtWidgets.QPushButton(self.frame_2)
        self.buttonPasteF.setToolTip("")
        self.buttonPasteF.setObjectName("buttonPasteF")
        self.gridLayout_3.addWidget(self.buttonPasteF, 0, 1, 1, 1)
        self.buttonPasteI = QtWidgets.QPushButton(self.frame_2)
        self.buttonPasteI.setObjectName("buttonPasteI")
        self.gridLayout_3.addWidget(self.buttonPasteI, 0, 2, 1, 1)
        self.buttonPasteO = QtWidgets.QPushButton(self.frame_2)
        self.buttonPasteO.setObjectName("buttonPasteO")
        self.gridLayout_3.addWidget(self.buttonPasteO, 0, 3, 1, 1)
        self.tableNames = QtWidgets.QTableWidget(self.frame_2)
        self.tableNames.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableNames.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableNames.setWordWrap(False)
        self.tableNames.setObjectName("tableNames")
        self.tableNames.setColumnCount(3)
        self.tableNames.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableNames.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNames.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableNames.setHorizontalHeaderItem(2, item)
        self.tableNames.horizontalHeader().setMinimumSectionSize(16)
        self.tableNames.horizontalHeader().setStretchLastSection(True)
        self.tableNames.verticalHeader().setDefaultSectionSize(21)
        self.tableNames.verticalHeader().setMinimumSectionSize(16)
        self.tableNames.verticalHeader().setStretchLastSection(False)
        self.gridLayout_3.addWidget(self.tableNames, 1, 0, 1, 4)
        self.gridNames.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLogins = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLogins.setSpacing(1)
        self.gridLogins.setContentsMargins(0, 0, 0, 0)
        self.gridLogins.setObjectName("gridLogins")
        self.frame = QtWidgets.QFrame(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkboxDisabled = QtWidgets.QCheckBox(self.frame)
        self.checkboxDisabled.setObjectName("checkboxDisabled")
        self.gridLayout_2.addWidget(self.checkboxDisabled, 4, 2, 1, 1)
        self.loginPrefix = QtWidgets.QLineEdit(self.frame)
        self.loginPrefix.setObjectName("loginPrefix")
        self.gridLayout_2.addWidget(self.loginPrefix, 0, 1, 1, 1)
        self.buttonCopyLogins = QtWidgets.QPushButton(self.frame)
        self.buttonCopyLogins.setObjectName("buttonCopyLogins")
        self.gridLayout_2.addWidget(self.buttonCopyLogins, 6, 3, 1, 1)
        self.loginTemplate = QtWidgets.QLineEdit(self.frame)
        self.loginTemplate.setText("")
        self.loginTemplate.setPlaceholderText("")
        self.loginTemplate.setObjectName("loginTemplate")
        self.gridLayout_2.addWidget(self.loginTemplate, 0, 2, 1, 1)
        self.lineEditAttribute = QtWidgets.QLineEdit(self.frame)
        self.lineEditAttribute.setPlaceholderText("")
        self.lineEditAttribute.setObjectName("lineEditAttribute")
        self.gridLayout_2.addWidget(self.lineEditAttribute, 2, 3, 1, 1)
        self.tableLogins = QtWidgets.QTableWidget(self.frame)
        self.tableLogins.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableLogins.setWordWrap(False)
        self.tableLogins.setObjectName("tableLogins")
        self.tableLogins.setColumnCount(3)
        self.tableLogins.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogins.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogins.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableLogins.setHorizontalHeaderItem(2, item)
        self.tableLogins.horizontalHeader().setMinimumSectionSize(16)
        self.tableLogins.horizontalHeader().setStretchLastSection(True)
        self.tableLogins.verticalHeader().setDefaultSectionSize(21)
        self.tableLogins.verticalHeader().setMinimumSectionSize(16)
        self.gridLayout_2.addWidget(self.tableLogins, 1, 1, 1, 3)
        self.passwordMask = QtWidgets.QLineEdit(self.frame)
        self.passwordMask.setText("")
        self.passwordMask.setObjectName("passwordMask")
        self.gridLayout_2.addWidget(self.passwordMask, 0, 3, 1, 1)
        self.comboBoxAttributes = QtWidgets.QComboBox(self.frame)
        self.comboBoxAttributes.setObjectName("comboBoxAttributes")
        self.gridLayout_2.addWidget(self.comboBoxAttributes, 2, 2, 1, 1)
        self.checkboxNotExpiredPass = QtWidgets.QCheckBox(self.frame)
        self.checkboxNotExpiredPass.setChecked(True)
        self.checkboxNotExpiredPass.setObjectName("checkboxNotExpiredPass")
        self.gridLayout_2.addWidget(self.checkboxNotExpiredPass, 4, 1, 1, 1)
        self.buttonGenLogins = QtWidgets.QPushButton(self.frame)
        self.buttonGenLogins.setObjectName("buttonGenLogins")
        self.gridLayout_2.addWidget(self.buttonGenLogins, 6, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
        self.comboboxGroups = QtWidgets.QComboBox(self.frame)
        self.comboboxGroups.setObjectName("comboboxGroups")
        self.gridLayout_2.addWidget(self.comboboxGroups, 3, 2, 1, 1)
        self.checkboxAddToGroup = QtWidgets.QCheckBox(self.frame)
        self.checkboxAddToGroup.setObjectName("checkboxAddToGroup")
        self.gridLayout_2.addWidget(self.checkboxAddToGroup, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)
        self.gridLogins.addWidget(self.frame, 0, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridAD = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridAD.setSpacing(1)
        self.gridAD.setContentsMargins(0, 0, 0, 0)
        self.gridAD.setObjectName("gridAD")
        self.frame_3 = QtWidgets.QFrame(self.gridLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.logBrowser = QtWidgets.QTextBrowser(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logBrowser.sizePolicy().hasHeightForWidth())
        self.logBrowser.setSizePolicy(sizePolicy)
        self.logBrowser.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.logBrowser.setObjectName("logBrowser")
        self.gridLayout_4.addWidget(self.logBrowser, 4, 0, 1, 3)
        self.adUser = QtWidgets.QLineEdit(self.frame_3)
        self.adUser.setObjectName("adUser")
        self.gridLayout_4.addWidget(self.adUser, 1, 1, 1, 1)
        self.buttonConnectToAD = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonConnectToAD.sizePolicy().hasHeightForWidth())
        self.buttonConnectToAD.setSizePolicy(sizePolicy)
        self.buttonConnectToAD.setObjectName("buttonConnectToAD")
        self.gridLayout_4.addWidget(self.buttonConnectToAD, 0, 0, 1, 3)
        self.adTree = QtWidgets.QTreeWidget(self.frame_3)
        self.adTree.setObjectName("adTree")
        self.adTree.headerItem().setText(0, "Выбери OU")
        self.gridLayout_4.addWidget(self.adTree, 3, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 5, 0, 1, 1)
        self.adPassword = QtWidgets.QLineEdit(self.frame_3)
        self.adPassword.setObjectName("adPassword")
        self.gridLayout_4.addWidget(self.adPassword, 1, 2, 1, 1)
        self.adServer = QtWidgets.QLineEdit(self.frame_3)
        self.adServer.setObjectName("adServer")
        self.gridLayout_4.addWidget(self.adServer, 1, 0, 1, 1)
        self.buttonCreateAccounts = QtWidgets.QPushButton(self.frame_3)
        self.buttonCreateAccounts.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCreateAccounts.sizePolicy().hasHeightForWidth())
        self.buttonCreateAccounts.setSizePolicy(sizePolicy)
        self.buttonCreateAccounts.setObjectName("buttonCreateAccounts")
        self.gridLayout_4.addWidget(self.buttonCreateAccounts, 2, 1, 1, 2)
        self.buttonTestAccounts = QtWidgets.QPushButton(self.frame_3)
        self.buttonTestAccounts.setEnabled(False)
        self.buttonTestAccounts.setObjectName("buttonTestAccounts")
        self.gridLayout_4.addWidget(self.buttonTestAccounts, 2, 0, 1, 1)
        self.gridAD.addWidget(self.frame_3, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.buttonPasteFIO, self.buttonPasteF)
        MainWindow.setTabOrder(self.buttonPasteF, self.buttonPasteI)
        MainWindow.setTabOrder(self.buttonPasteI, self.buttonPasteO)
        MainWindow.setTabOrder(self.buttonPasteO, self.tableNames)
        MainWindow.setTabOrder(self.tableNames, self.loginPrefix)
        MainWindow.setTabOrder(self.loginPrefix, self.loginTemplate)
        MainWindow.setTabOrder(self.loginTemplate, self.passwordMask)
        MainWindow.setTabOrder(self.passwordMask, self.tableLogins)
        MainWindow.setTabOrder(self.tableLogins, self.comboBoxAttributes)
        MainWindow.setTabOrder(self.comboBoxAttributes, self.lineEditAttribute)
        MainWindow.setTabOrder(self.lineEditAttribute, self.comboboxGroups)
        MainWindow.setTabOrder(self.comboboxGroups, self.checkboxAddToGroup)
        MainWindow.setTabOrder(self.checkboxAddToGroup, self.checkboxNotExpiredPass)
        MainWindow.setTabOrder(self.checkboxNotExpiredPass, self.checkboxDisabled)
        MainWindow.setTabOrder(self.checkboxDisabled, self.buttonGenLogins)
        MainWindow.setTabOrder(self.buttonGenLogins, self.buttonCopyLogins)
        MainWindow.setTabOrder(self.buttonCopyLogins, self.buttonConnectToAD)
        MainWindow.setTabOrder(self.buttonConnectToAD, self.adServer)
        MainWindow.setTabOrder(self.adServer, self.adUser)
        MainWindow.setTabOrder(self.adUser, self.adPassword)
        MainWindow.setTabOrder(self.adPassword, self.buttonTestAccounts)
        MainWindow.setTabOrder(self.buttonTestAccounts, self.buttonCreateAccounts)
        MainWindow.setTabOrder(self.buttonCreateAccounts, self.adTree)
        MainWindow.setTabOrder(self.adTree, self.logBrowser)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.buttonPasteFIO.setText(QtWidgets.QApplication.translate("MainWindow", "Вставить ФИО", None, -1))
        self.buttonPasteF.setText(QtWidgets.QApplication.translate("MainWindow", "Только Ф", None, -1))
        self.buttonPasteI.setText(QtWidgets.QApplication.translate("MainWindow", "Только И", None, -1))
        self.buttonPasteO.setText(QtWidgets.QApplication.translate("MainWindow", "Только О", None, -1))
        self.tableNames.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Фамилия", None, -1))
        self.tableNames.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Имя", None, -1))
        self.tableNames.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Отчество", None, -1))
        self.checkboxDisabled.setText(QtWidgets.QApplication.translate("MainWindow", "Disabled", None, -1))
        self.loginPrefix.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "Префикс логина", None, -1))
        self.buttonCopyLogins.setText(QtWidgets.QApplication.translate("MainWindow", "Скопировать всё", None, -1))
        self.loginTemplate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">f</span> - фамилия<br/><span style=\" font-weight:600;\">i</span> - имя<br/><span style=\" font-weight:600;\">o</span> - отчество<br/><br/>Используйте цифры, например:<br/><span style=\" font-weight:600;\">i2</span> - две первых буквы имени (транслитерированного)<br/><br/><span style=\" font-weight:600;\">f_i1o1</span> - Ivanov_II</p></body></html>", None, -1))
        self.tableLogins.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "DisplayName", None, -1))
        self.tableLogins.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Login", None, -1))
        self.tableLogins.horizontalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Password", None, -1))
        self.passwordMask.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>! - БОЛЬШАЯ БУКВА<br/>@ - маленькая буква<br/># - цифра<br/>$ - знак пунктуации<br/><br/>Например:<br/>!@###$### - Rd834)214</p></body></html>", None, -1))
        self.checkboxNotExpiredPass.setText(QtWidgets.QApplication.translate("MainWindow", "Not Expired Pass", None, -1))
        self.buttonGenLogins.setText(QtWidgets.QApplication.translate("MainWindow", "Генерировать", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Общие аттрибуты:", None, -1))
        self.checkboxAddToGroup.setText(QtWidgets.QApplication.translate("MainWindow", "Добавить", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Добавить в группы:", None, -1))
        self.adUser.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "user", None, -1))
        self.buttonConnectToAD.setText(QtWidgets.QApplication.translate("MainWindow", "Соединиться с AD по-умолчанию, или:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">Homepage: </span><a href=\"https://github.com/qiwichupa/RussianFIO2AD\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">https://github.com/qiwichupa/RussianFIO2AD</span></a><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\"><br /><br />Icons by </span><a href=\"https://www.freepik.com/\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">Freepik</span></a><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">, </span><a href=\"https://www.flaticon.com/authors/prettycons\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">prettycons</span></a><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\"> <br />from </span><a href=\"https://www.flaticon.com/\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">www.flaticon.com</span></a><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\"> is licensed by </span><a href=\"http://creativecommons.org/licenses/by/3.0/\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt; text-decoration: underline; color:#0000ff;\">CC 3.0 BY</span></a></p></body></html>", None, -1))
        self.adPassword.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "password", None, -1))
        self.adServer.setPlaceholderText(QtWidgets.QApplication.translate("MainWindow", "ad controller", None, -1))
        self.buttonCreateAccounts.setText(QtWidgets.QApplication.translate("MainWindow", "Создать аккаунты в:", None, -1))
        self.buttonTestAccounts.setToolTip(QtWidgets.QApplication.translate("MainWindow", "<html><head/><body><p>Предварительная проверка на повторы: <br/>sAMAccountName - глобально, <br/>distinguishedName - внутри выбранной OU рекурсивно</p></body></html>", None, -1))
        self.buttonTestAccounts.setText(QtWidgets.QApplication.translate("MainWindow", "Проверка на дубли", None, -1))

import icons_rc
