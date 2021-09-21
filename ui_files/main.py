# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 533)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1100, 0))
        MainWindow.setBaseSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/icons/icons/main.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy2)
        self.splitter.setLayoutDirection(Qt.LeftToRight)
        self.splitter.setFrameShape(QFrame.NoFrame)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(5)
        self.splitter.setChildrenCollapsible(False)
        self.gridLayoutWidget_2 = QWidget(self.splitter)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridNames = QGridLayout(self.gridLayoutWidget_2)
        self.gridNames.setSpacing(1)
        self.gridNames.setObjectName(u"gridNames")
        self.gridNames.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.gridLayoutWidget_2)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy3)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.buttonPasteFIO = QPushButton(self.frame_2)
        self.buttonPasteFIO.setObjectName(u"buttonPasteFIO")

        self.gridLayout_3.addWidget(self.buttonPasteFIO, 0, 0, 1, 1)

        self.buttonPasteF = QPushButton(self.frame_2)
        self.buttonPasteF.setObjectName(u"buttonPasteF")

        self.gridLayout_3.addWidget(self.buttonPasteF, 0, 1, 1, 1)

        self.buttonPasteI = QPushButton(self.frame_2)
        self.buttonPasteI.setObjectName(u"buttonPasteI")

        self.gridLayout_3.addWidget(self.buttonPasteI, 0, 2, 1, 1)

        self.buttonPasteO = QPushButton(self.frame_2)
        self.buttonPasteO.setObjectName(u"buttonPasteO")

        self.gridLayout_3.addWidget(self.buttonPasteO, 0, 3, 1, 1)

        self.tableNames = QTableWidget(self.frame_2)
        if (self.tableNames.columnCount() < 3):
            self.tableNames.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableNames.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableNames.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableNames.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableNames.setObjectName(u"tableNames")
        self.tableNames.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableNames.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableNames.setWordWrap(False)
        self.tableNames.horizontalHeader().setMinimumSectionSize(16)
        self.tableNames.horizontalHeader().setStretchLastSection(True)
        self.tableNames.verticalHeader().setMinimumSectionSize(16)
        self.tableNames.verticalHeader().setDefaultSectionSize(21)
        self.tableNames.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tableNames, 1, 0, 1, 4)


        self.gridNames.addWidget(self.frame_2, 0, 0, 1, 1)

        self.splitter.addWidget(self.gridLayoutWidget_2)
        self.gridLayoutWidget = QWidget(self.splitter)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLogins = QGridLayout(self.gridLayoutWidget)
        self.gridLogins.setSpacing(1)
        self.gridLogins.setObjectName(u"gridLogins")
        self.gridLogins.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.gridLayoutWidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkboxDisabled = QCheckBox(self.frame)
        self.checkboxDisabled.setObjectName(u"checkboxDisabled")

        self.gridLayout_2.addWidget(self.checkboxDisabled, 4, 2, 1, 1)

        self.loginPrefix = QLineEdit(self.frame)
        self.loginPrefix.setObjectName(u"loginPrefix")

        self.gridLayout_2.addWidget(self.loginPrefix, 0, 1, 1, 1)

        self.buttonCopyLogins = QPushButton(self.frame)
        self.buttonCopyLogins.setObjectName(u"buttonCopyLogins")

        self.gridLayout_2.addWidget(self.buttonCopyLogins, 6, 3, 1, 1)

        self.loginTemplate = QLineEdit(self.frame)
        self.loginTemplate.setObjectName(u"loginTemplate")

        self.gridLayout_2.addWidget(self.loginTemplate, 0, 2, 1, 1)

        self.lineEditAttribute = QLineEdit(self.frame)
        self.lineEditAttribute.setObjectName(u"lineEditAttribute")

        self.gridLayout_2.addWidget(self.lineEditAttribute, 2, 3, 1, 1)

        self.tableLogins = QTableWidget(self.frame)
        if (self.tableLogins.columnCount() < 3):
            self.tableLogins.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableLogins.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableLogins.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableLogins.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableLogins.setObjectName(u"tableLogins")
        self.tableLogins.setMinimumSize(QSize(400, 0))
        self.tableLogins.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableLogins.setWordWrap(False)
        self.tableLogins.horizontalHeader().setMinimumSectionSize(16)
        self.tableLogins.horizontalHeader().setStretchLastSection(True)
        self.tableLogins.verticalHeader().setMinimumSectionSize(16)
        self.tableLogins.verticalHeader().setDefaultSectionSize(21)

        self.gridLayout_2.addWidget(self.tableLogins, 1, 1, 1, 3)

        self.passwordMask = QLineEdit(self.frame)
        self.passwordMask.setObjectName(u"passwordMask")

        self.gridLayout_2.addWidget(self.passwordMask, 0, 3, 1, 1)

        self.comboBoxAttributes = QComboBox(self.frame)
        self.comboBoxAttributes.setObjectName(u"comboBoxAttributes")

        self.gridLayout_2.addWidget(self.comboBoxAttributes, 2, 2, 1, 1)

        self.checkboxNotExpiredPass = QCheckBox(self.frame)
        self.checkboxNotExpiredPass.setObjectName(u"checkboxNotExpiredPass")
        self.checkboxNotExpiredPass.setChecked(True)

        self.gridLayout_2.addWidget(self.checkboxNotExpiredPass, 4, 1, 1, 1)

        self.buttonGenLogins = QPushButton(self.frame)
        self.buttonGenLogins.setObjectName(u"buttonGenLogins")

        self.gridLayout_2.addWidget(self.buttonGenLogins, 6, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)

        self.comboboxGroups = QComboBox(self.frame)
        self.comboboxGroups.setObjectName(u"comboboxGroups")

        self.gridLayout_2.addWidget(self.comboboxGroups, 3, 2, 1, 1)

        self.checkboxAddToGroup = QCheckBox(self.frame)
        self.checkboxAddToGroup.setObjectName(u"checkboxAddToGroup")

        self.gridLayout_2.addWidget(self.checkboxAddToGroup, 3, 3, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 3, 1, 1, 1)


        self.gridLogins.addWidget(self.frame, 0, 1, 1, 1)

        self.splitter.addWidget(self.gridLayoutWidget)
        self.gridLayoutWidget_3 = QWidget(self.splitter)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridAD = QGridLayout(self.gridLayoutWidget_3)
        self.gridAD.setSpacing(0)
        self.gridAD.setObjectName(u"gridAD")
        self.gridAD.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridAD.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.gridLayoutWidget_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_3)
        self.gridLayout_4.setSpacing(1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.logBrowser = QTextBrowser(self.frame_3)
        self.logBrowser.setObjectName(u"logBrowser")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.logBrowser.sizePolicy().hasHeightForWidth())
        self.logBrowser.setSizePolicy(sizePolicy4)
        self.logBrowser.setLineWrapMode(QTextEdit.NoWrap)

        self.gridLayout_4.addWidget(self.logBrowser, 4, 0, 1, 3)

        self.adUser = QLineEdit(self.frame_3)
        self.adUser.setObjectName(u"adUser")

        self.gridLayout_4.addWidget(self.adUser, 1, 1, 1, 1)

        self.buttonConnectToAD = QPushButton(self.frame_3)
        self.buttonConnectToAD.setObjectName(u"buttonConnectToAD")
        self.buttonConnectToAD.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.buttonConnectToAD.sizePolicy().hasHeightForWidth())
        self.buttonConnectToAD.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.buttonConnectToAD, 0, 0, 1, 3)

        self.adTree = QTreeWidget(self.frame_3)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"\u0412\u044b\u0431\u0435\u0440\u0438 OU");
        self.adTree.setHeaderItem(__qtreewidgetitem)
        self.adTree.setObjectName(u"adTree")
        sizePolicy4.setHeightForWidth(self.adTree.sizePolicy().hasHeightForWidth())
        self.adTree.setSizePolicy(sizePolicy4)

        self.gridLayout_4.addWidget(self.adTree, 3, 0, 1, 3)

        self.adPassword = QLineEdit(self.frame_3)
        self.adPassword.setObjectName(u"adPassword")

        self.gridLayout_4.addWidget(self.adPassword, 1, 2, 1, 1)

        self.adServer = QLineEdit(self.frame_3)
        self.adServer.setObjectName(u"adServer")
        sizePolicy5.setHeightForWidth(self.adServer.sizePolicy().hasHeightForWidth())
        self.adServer.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.adServer, 1, 0, 1, 1)

        self.buttonCreateAccounts = QPushButton(self.frame_3)
        self.buttonCreateAccounts.setObjectName(u"buttonCreateAccounts")
        self.buttonCreateAccounts.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.buttonCreateAccounts.sizePolicy().hasHeightForWidth())
        self.buttonCreateAccounts.setSizePolicy(sizePolicy6)

        self.gridLayout_4.addWidget(self.buttonCreateAccounts, 2, 1, 1, 2)

        self.buttonTestAccounts = QPushButton(self.frame_3)
        self.buttonTestAccounts.setObjectName(u"buttonTestAccounts")
        self.buttonTestAccounts.setEnabled(False)

        self.gridLayout_4.addWidget(self.buttonTestAccounts, 2, 0, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)

        self.gridLayout_4.addWidget(self.label, 5, 0, 1, 3)


        self.gridAD.addWidget(self.frame_3, 2, 3, 1, 1)

        self.splitter.addWidget(self.gridLayoutWidget_3)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.buttonPasteFIO, self.buttonPasteF)
        QWidget.setTabOrder(self.buttonPasteF, self.buttonPasteI)
        QWidget.setTabOrder(self.buttonPasteI, self.buttonPasteO)
        QWidget.setTabOrder(self.buttonPasteO, self.tableNames)
        QWidget.setTabOrder(self.tableNames, self.loginPrefix)
        QWidget.setTabOrder(self.loginPrefix, self.loginTemplate)
        QWidget.setTabOrder(self.loginTemplate, self.passwordMask)
        QWidget.setTabOrder(self.passwordMask, self.tableLogins)
        QWidget.setTabOrder(self.tableLogins, self.comboBoxAttributes)
        QWidget.setTabOrder(self.comboBoxAttributes, self.lineEditAttribute)
        QWidget.setTabOrder(self.lineEditAttribute, self.comboboxGroups)
        QWidget.setTabOrder(self.comboboxGroups, self.checkboxAddToGroup)
        QWidget.setTabOrder(self.checkboxAddToGroup, self.checkboxNotExpiredPass)
        QWidget.setTabOrder(self.checkboxNotExpiredPass, self.checkboxDisabled)
        QWidget.setTabOrder(self.checkboxDisabled, self.buttonGenLogins)
        QWidget.setTabOrder(self.buttonGenLogins, self.buttonCopyLogins)
        QWidget.setTabOrder(self.buttonCopyLogins, self.buttonConnectToAD)
        QWidget.setTabOrder(self.buttonConnectToAD, self.adServer)
        QWidget.setTabOrder(self.adServer, self.adUser)
        QWidget.setTabOrder(self.adUser, self.adPassword)
        QWidget.setTabOrder(self.adPassword, self.buttonTestAccounts)
        QWidget.setTabOrder(self.buttonTestAccounts, self.buttonCreateAccounts)
        QWidget.setTabOrder(self.buttonCreateAccounts, self.adTree)
        QWidget.setTabOrder(self.adTree, self.logBrowser)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.buttonPasteFIO.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.buttonPasteFIO.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0424\u0418\u041e", None))
#if QT_CONFIG(tooltip)
        self.buttonPasteF.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.buttonPasteF.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e \u0424", None))
        self.buttonPasteI.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e \u0418", None))
        self.buttonPasteO.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043b\u044c\u043a\u043e \u041e", None))
        ___qtablewidgetitem = self.tableNames.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem1 = self.tableNames.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem2 = self.tableNames.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        self.checkboxDisabled.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.loginPrefix.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0444\u0438\u043a\u0441 \u043b\u043e\u0433\u0438\u043d\u0430", None))
        self.buttonCopyLogins.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432\u0441\u0451", None))
#if QT_CONFIG(tooltip)
        self.loginTemplate.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">f</span> - \u0444\u0430\u043c\u0438\u043b\u0438\u044f<br/><span style=\" font-weight:600;\">i</span> - \u0438\u043c\u044f<br/><span style=\" font-weight:600;\">o</span> - \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e<br/><br/>\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 \u0446\u0438\u0444\u0440\u044b, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440:<br/><span style=\" font-weight:600;\">i2</span> - \u0434\u0432\u0435 \u043f\u0435\u0440\u0432\u044b\u0445 \u0431\u0443\u043a\u0432\u044b \u0438\u043c\u0435\u043d\u0438 (\u0442\u0440\u0430\u043d\u0441\u043b\u0438\u0442\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e)<br/><br/><span style=\" font-weight:600;\">f_i1o1</span> - Ivanov_II</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.loginTemplate.setText("")
        self.loginTemplate.setPlaceholderText("")
        self.lineEditAttribute.setPlaceholderText("")
        ___qtablewidgetitem3 = self.tableLogins.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DisplayName", None));
        ___qtablewidgetitem4 = self.tableLogins.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Login", None));
        ___qtablewidgetitem5 = self.tableLogins.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Password", None));
#if QT_CONFIG(tooltip)
        self.passwordMask.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>! - \u0411\u041e\u041b\u042c\u0428\u0410\u042f \u0411\u0423\u041a\u0412\u0410<br/>@ - \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u0430\u044f \u0431\u0443\u043a\u0432\u0430<br/># - \u0446\u0438\u0444\u0440\u0430<br/>$ - \u0437\u043d\u0430\u043a \u043f\u0443\u043d\u043a\u0442\u0443\u0430\u0446\u0438\u0438<br/><br/>\u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440:<br/>!@###$### - Rd834)214</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.passwordMask.setText("")
        self.checkboxNotExpiredPass.setText(QCoreApplication.translate("MainWindow", u"Not Expired Pass", None))
        self.buttonGenLogins.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u0430\u0442\u0442\u0440\u0438\u0431\u0443\u0442\u044b:", None))
        self.checkboxAddToGroup.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0433\u0440\u0443\u043f\u043f\u044b:", None))
        self.adUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"user", None))
        self.buttonConnectToAD.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0435\u0434\u0438\u043d\u0438\u0442\u044c\u0441\u044f \u0441 AD \u043f\u043e-\u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e, \u0438\u043b\u0438:", None))
        self.adPassword.setPlaceholderText(QCoreApplication.translate("MainWindow", u"password", None))
        self.adServer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ad controller", None))
        self.buttonCreateAccounts.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u044b \u0432:", None))
#if QT_CONFIG(tooltip)
        self.buttonTestAccounts.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043d\u0430 \u043f\u043e\u0432\u0442\u043e\u0440\u044b: <br/>sAMAccountName - \u0433\u043b\u043e\u0431\u0430\u043b\u044c\u043d\u043e, <br/>distinguishedName - \u0432\u043d\u0443\u0442\u0440\u0438 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0439 OU \u0440\u0435\u043a\u0443\u0440\u0441\u0438\u0432\u043d\u043e</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.buttonTestAccounts.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043d\u0430 \u0434\u0443\u0431\u043b\u0438", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Homepage: <br /><a href=\"https://github.com/qiwichupa/RussianFIO2AD\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/qiwichupa/RussianFIO2AD</span></a><br /><br />Icons by <a href=\"https://www.freepik.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Freepik</span></a>, <a href=\"https://www.flaticon.com/authors/prettycons\"><span style=\" text-decoration: underline; color:#0000ff;\">prettycons</span></a> <br />from <a href=\"https://www.flaticon.com/\"><span style=\" text-decoration: underline; color:#0000ff"
                        ";\">www.flaticon.com</span></a> is licensed by <a href=\"http://creativecommons.org/licenses/by/3.0/\"><span style=\" text-decoration: underline; color:#0000ff;\">CC 3.0 BY</span></a></p></body></html>", None))
    # retranslateUi

