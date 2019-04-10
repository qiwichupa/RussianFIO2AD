import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets


import logging
import os

from pyad import pyad
import pyad.adquery
import random
import regex
import string
import sys

import utilities

from ui_files import pyMain


__appname__ = "RussianFIO2AD"
__version__ = "0.0.6"


# get path of program dir.
# sys._MEIPASS - variable of pyinstaller (one-dir package) with path to executable
try:
    sys._MEIPASS
    appPath = sys._MEIPASS
except:
    appPath =  os.path.dirname(os.path.abspath(__file__))

# set "data" in program dir as working directory
appDataPath = os.path.join(appPath, "data")
try:
    os.makedirs(appDataPath, exist_ok=True)
except:
    appDataPath = appPath

logfile = os.path.join(appDataPath, __appname__ + ".log")

# remove large logfile
logFileSizeLimit = 8 # MB
try:
    os.stat(logfile).st_size
    if os.stat(logfile).st_size > logFileSizeLimit*1024**2:
        removedLogFileSize = os.stat(logfile).st_size
        try:
            os.remove(logfile)
        except:
            pass
except:
    pass

# logging
logging.basicConfig(handlers=[logging.FileHandler(logfile, 'a', 'utf-8-sig')],
                    format="%(asctime)-15s\t%(name)-10s\t%(levelname)-8s\t%(module)-10s\t%(funcName)-35s\t%(lineno)-6d\t%(message)s",
                    level=logging.DEBUG)
logger = logging.getLogger(name="main-gui")
#sys.stdout = utilities.LoggerWriter(logger.warning)
sys.stderr = utilities.LoggerWriter(logger.warning)
try:
    removedLogFileSize
    logger.info("Previous logfile was removed by size limit (" + str(logFileSizeLimit) + "MB). Size was: " + str(removedLogFileSize) + " bytes.")
except:
    pass


class Main(QtWidgets.QMainWindow, pyMain.Ui_MainWindow):

    commonAttributes = {}
    groups = {}

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle(__appname__ + " (v. " + __version__ + ")")

        self.settings = QtCore.QSettings(os.path.join(appDataPath, "settings.ini"), QtCore.QSettings.IniFormat)
        self.settings.setIniCodec("UTF-8")

        self.clip = QtGui.QClipboard()
        self.adTree.itemClicked.connect(self.adTreeItemClicked)

        self.buttonPasteFIO.clicked.connect(self.buttonPasteFIOClicked)
        self.buttonPasteF.clicked.connect(self.buttonPasteFClicked)
        self.buttonPasteI.clicked.connect(self.buttonPasteIClicked)
        self.buttonPasteO.clicked.connect(self.buttonPasteOClicked)

        self.loginTemplate.textEdited.connect(self.loginTemplateEmitted)
        self.passwordMask.textEdited.connect(self.passwordMaskEmitted)

        self.buttonGenLogins.clicked.connect(self.buttonGenLoginsClicked)
        self.buttonCopyLogins.clicked.connect(self.copySelectedToClipboard)

        self.lineEditAttribute.textEdited.connect(self.lineEditAttributeEmitted)
        self.comboBoxAttributes.activated.connect(self.comboBoxAttributesActivated)

        self.checkboxAddToGroup.stateChanged.connect(self.checkboxAddToGroupStateChanged)
        self.comboboxGroups.activated.connect(self.comboboxGroupsActivated)

        self.buttonConnectToAD.clicked.connect(self.buttonConnectToADClicked)
        self.buttonCreateAccounts.clicked.connect(self.createADAccounts)

        self.buttonConnectToAD.hide()
        self.adServer.hide()
        self.adUser.hide()
        self.adPassword.hide()

        self.loadAdToUI()

        self.initSettings()

    def initSettings(self):
        if not self.settings.value("templLogin"):
            self.settings.setValue("templLogin", "f_i1o1")
        if not self.settings.value("templPassword"):
            self.settings.setValue("templPassword", "!@#$##$#")
        if not self.settings.value("commonAttributes"):
            self.settings.setValue("commonAttributes", "description,company,department")

        for key in self.settings.value("commonAttributes").split(","):
            self.commonAttributes[key] = ""
            self.comboBoxAttributes.addItems([key])

        self.loginTemplate.setText(self.settings.value("templLogin"))
        self.passwordMask.setText(self.settings.value("templPassword"))

    def refreshADGroups(self):
        q = pyad.adquery.ADQuery()

        q.execute_query(
            attributes=["distinguishedName", "cn"],
            where_clause="objectClass = 'group'"
            )

        self.groups = {}
        for group in q.get_results():
            if "\\" not in group["distinguishedName"]:
                cn = group["cn"]
                dn = group["distinguishedName"]
                self.groups[cn] = [dn, False]

        for cn in sorted(self.groups.keys()):
            self.comboboxGroups.addItems([cn])

    def comboboxGroupsActivated(self):
        cn = self.comboboxGroups.currentText()
        self.checkboxAddToGroup.setChecked(self.groups[cn][1])

    def checkboxAddToGroupStateChanged(self):
        currentCN = self.comboboxGroups.currentText()

        if self.checkboxAddToGroup.isChecked():
            self.groups[currentCN][1] = True
        else:
            self.groups[currentCN][1] = False

        # refresh list, selected on top
        self.comboboxGroups.clear()
        n=0
        for cn in sorted(self.groups.keys()):
            if self.groups[cn][1] == True:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icons/icons/edited.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.comboboxGroups.addItem(cn)
                self.comboboxGroups.setItemIcon(n, icon)
                n += 1
        for cn in sorted(self.groups.keys()):
            if self.groups[cn][1] == False:
                self.comboboxGroups.addItem(cn)

        self.comboboxGroups.setCurrentText(currentCN)

    def lineEditAttributeEmitted(self):
        """Changes the value of an attribute variable. Marks a non-empty list item"""
        key = self.comboBoxAttributes.currentText()
        self.commonAttributes[key] = self.lineEditAttribute.text().strip()
        if self.lineEditAttribute.text().strip() != "":
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/edited.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon = QtGui.QIcon()
        self.comboBoxAttributes.setItemIcon(self.comboBoxAttributes.currentIndex(), icon)

    def loginTemplateEmitted(self):
        self.settings.setValue("templLogin", self.loginTemplate.text())

    def passwordMaskEmitted(self):
        self.settings.setValue("templPassword", self.passwordMask.text())

    def comboBoxAttributesActivated(self):
        key = self.comboBoxAttributes.currentText()
        self.lineEditAttribute.setText(self.commonAttributes[key])

    def buttonConnectToADClicked(self):
        pass

    def loadAdToUI(self):
        try:
            adOUs = self.get_ad_tree()
        except Exception as e:
            print(str(e))
        else:
            list = self.tree_widget_list(adOUs)
            self.adTree.insertTopLevelItems(0, list)

            self.refreshADGroups()

    def adTreeItemClicked(self):
        item = self.adTree.selectedItems()
        if item:
            self.buttonCreateAccounts.setEnabled(True)
            selectedText = item[0].text(0)

            parents = []
            for index in self.adTree.selectedIndexes():
                while index.parent().isValid():
                    index = index.parent()
                    parents = [index.sibling(index.row(), 0).data()] + parents

            self.adPathListReversed = parents + [selectedText]
            self.adPathList = list(reversed(self.adPathListReversed))
            self.adTree.setHeaderLabel("/".join(self.adPathListReversed))

    def createADAccounts(self):
        self.buttonCreateAccounts.setDisabled(True)
        if self.adPathList:
            domain = "DC=" + ",DC=".join(self.domainList)
            organizationUnitDN = "OU=" + ",OU=".join(self.adPathList) + "," + domain
            container = utilities.get_container_from_dn(organizationUnitDN)


            self.logBrowser.append("""===================\nCreating in "{}"\n===================""".format("/".join(self.adPathListReversed)))
            logger.info("""\n===================\nCreating in "{}"\n===================""".format("/".join(self.adPathListReversed)))
            users = []
            for i in range(0, self.tableLogins.rowCount()):

                displayName = self.tableLogins.item(i, 0).text().strip()
                login = self.tableLogins.item(i, 1).text().strip()
                password = self.tableLogins.item(i, 2).text().strip()

                if displayName != "" and login != "" and password != "":
                    users += [{"displayName": displayName, "login": login, "password": password}]
                    self.add_user_to_ad(displayName, login, password, container)
                else:
                    self.logBrowser.append("\nПропуск: {} {} {} - пустое поле\n".format(displayName, login, password))

            self.buttonCreateAccounts.setEnabled(True)

    def add_user_to_ad(self, displayName, login, password, container):
        basicAttributes = {
                             "displayName": displayName,
                             "sAMAccountName": login,
                             "userPrincipalName": login + "@" + ".".join(self.domainList)
                           }

        optionalAttributes = {}
        for key in self.commonAttributes.keys():
            if self.commonAttributes[key].strip() != "":
                optionalAttributes[key] = self.commonAttributes[key].strip()

        attributes = {**basicAttributes, **optionalAttributes}
        try:
            logger.info("""Создание: {} """.format(str(attributes)))
            user = pyad.aduser.ADUser.create(displayName, container, password=password, optional_attributes=attributes)
        except Exception as e:
            self.logBrowser.append("""Ошибка: {}({}: {}, {})\n """.format(str(e), displayName, password, str(container)))
            logger.warning("""Ошибка: {}({}: {}, {}) """.format(str(e), displayName, password, str(container)))
            try:
                user.delete()
            except:
                pass
        else:
            self.logBrowser.append("""Создана учетная запись "{}": {}, {} """.format(displayName, password, str(container)))
            logger.info("""Создана учетная запись "{}": {}, {} """.format(displayName, password, str(container)))

            if self.checkboxNotExpiredPass.isChecked():
                try:
                    logger.info("""Установка флага пароля "not expired" """)
                    user.set_user_account_control_setting("DONT_EXPIRE_PASSWD", True)
                except Exception as e:
                    self.logBrowser.append("""Ошибка установки флага пароля "not expired": {}""".format(str(e)))
                    logger.warning("""Ошибка установки флага пароля "not expired": {}""".format(str(e)))
                else:
                    logger.info("""Флаг установлен""")
            if self.checkboxDisabled.isChecked():
                try:
                    logger.info("""Установка флага пароля "disabled" """)
                    pyad.adobject.ADObject.disable(user)
                except Exception as e:
                    self.logBrowser.append("""Ошибка установки флага "disabled": {}""".format(str(e)))
                    logger.warning("""Ошибка установки флага "disabled": {}""".format(str(e)))
                else:
                    logger.info("""Флаг установлен""")
            for cn in self.groups.keys():
                if self.groups[cn][1] == True:
                    try:
                        logger.info("""Получение объекта группы: {}""".format(self.groups[cn][0]))
                        group = pyad.adgroup.ADGroup.from_dn(self.groups[cn][0])
                    except Exception as e:
                        self.logBrowser.append("""Ошибка": {}""".format(str(e)))
                        logger.warning("""Ошибка": {}""".format(str(e)))
                    else:
                        logger.info("""Объект получен: {}""".format(str(group)))
                        try:
                            logger.info("""Добавление учетной записи в группу""")
                            group.add_members([user])
                        except Exception as e:
                            self.logBrowser.append("""Ошибка": {}""".format(str(e)))
                            logger.warning("""Ошибка": {}""".format(str(e)))
                        else:
                            logger.info("""Учетная запись добавлена в группу""")

    def get_ad_tree(self):
        try:
            query = pyad.adquery.ADQuery()
            query.execute_query(
                attributes=["distinguishedName", "description"],
                where_clause="objectClass = 'organizationalUnit'"
                )
        except Exception as e:
            raise Exception(str(e))
        else:
            domain = False
            ous = []
            for row in query.get_results():

                while domain == False:
                    self.domainList = row["distinguishedName"].split(",DC=", maxsplit=1)[1].split(",DC=")
                    domain = ".".join(self.domainList)
                    self.logBrowser.append("Domain: " + domain)
                pathList = regex.subf("^OU=", "", row["distinguishedName"].split(",DC=")[0]).split(",OU=")
                reversedPathList = list(reversed(pathList))
                """
                incorrectChars = ["\\"] # Некорректно обрабатываются при попытке обратиться к контейнеру в процессе создания учеток
                if any(True for x in incorrectChars if x in "".join(reversedPathList)):
                    pass
                else:
                    ous += [reversedPathList]
                """
                ous += [reversedPathList]
            return ous

    def tree_widget_list(self, show_list):
        """
        Creates a list for updating tree widget
        :param show_list:
        :return:
        """
        items = []
        for item_parts in show_list:

            entry = QtWidgets.QTreeWidgetItem(None, [item_parts[0]])
            items_text = [i.text(0) for i in items]
            if entry.text(0) not in items_text:
                parent_item = entry
            else:
                parent_index = items_text.index(entry.text(0))
                parent_item = items[parent_index]

            if len(item_parts) > 1:
                for i in item_parts[1:]:
                    child_item = QtWidgets.QTreeWidgetItem(None, [i])
                    child_list_text = [parent_item.child(i).text(0) for i in range(parent_item.childCount())]
                    if child_item.text(0) in child_list_text:
                        child_index = child_list_text.index(child_item.text(0))
                        parent_item = parent_item.child(child_index)
                    else:
                        parent_item.addChild(child_item)
                        parent_item = child_item
            items.append(entry) if entry.text(0) not in items_text else None
        return items

    def buttonPasteFClicked(self):
        clipboard = self.clip.text().splitlines()

        row = 0
        for f in clipboard:
            f = f.strip()
            if row >= self.tableNames.rowCount():
                self.tableNames.insertRow(row)
            self.tableNames.setItem(row, 0, QtWidgets.QTableWidgetItem(f))
            row += 1

    def buttonPasteIClicked(self):
        clipboard = self.clip.text().splitlines()

        row = 0
        for f in clipboard:
            f = f.strip()
            if row >= self.tableNames.rowCount():
                self.tableNames.insertRow(row)
            self.tableNames.setItem(row, 1, QtWidgets.QTableWidgetItem(f))
            row += 1

    def buttonPasteOClicked(self):
        clipboard = self.clip.text().splitlines()

        row = 0
        for f in clipboard:
            f = f.strip()
            if row >= self.tableNames.rowCount():
                self.tableNames.insertRow(row)
            self.tableNames.setItem(row, 2, QtWidgets.QTableWidgetItem(f))
            row += 1

    def buttonPasteFIOClicked(self):
        """Fills FIO table from clipboard"""
        clipboard = self.clip.text().splitlines()
        self.tableNames.setRowCount(0)

        for fio in clipboard:
            try:
                fioSplitted = self.split_fio(fio)
            except:
                pass
            else:
                row = self.tableNames.rowCount()
                self.tableNames.insertRow(row)

                for n in range(1, len(fioSplitted)+1):
                    t = fioSplitted[n-1].strip()
                    self.tableNames.setItem(row, n-1, QtWidgets.QTableWidgetItem(t))

    def buttonGenLoginsClicked(self):
        self.tableLogins.setRowCount(0)
        for fioRow in range(0, self.tableNames.rowCount()):
            row = self.tableLogins.rowCount()
            self.tableLogins.insertRow(row)

            f = self.tableNames.item(fioRow, 0).text()
            i = self.tableNames.item(fioRow, 1).text()
            o = self.tableNames.item(fioRow, 2).text()
            fio = "{} {} {}".format(f,i,o)
            password = self.password_templating()

            login = self.login_templating(f,i,o)[:24]

            self.tableLogins.setItem(row, 0, QtWidgets.QTableWidgetItem(fio))
            self.tableLogins.setItem(row, 1, QtWidgets.QTableWidgetItem(login))
            self.tableLogins.setItem(row, 2, QtWidgets.QTableWidgetItem(password))

    def split_fio(self, fio):
        """Returns splitted FIO if string can be splitted"""
        result = fio.strip().split("\t", maxsplit=3)
        if len(result) > 1:
            return result


        result = fio.strip().split(" ", maxsplit=3)
        if len(result) > 1:
            return result

        raise Exception

    def login_templating(self, f,i,o):
        fLat = utilities.translit(f)
        iLat = utilities.translit(i)
        oLat = utilities.translit(o)
        template = self.loginTemplate.text()

        template = regex.subf(r'([fio])(\d*)', '{{{1}:.{2}}}', template)
        template = template.replace(":.}", "}")

        login = self.loginPrefix.text() + template.format(f=fLat, i=iLat, o=oLat)

        return login

    def password_templating(self):

        template = self.passwordMask.text()
        password = ""

        for i in template:
            if i == "!":
                password += random.choice(string.ascii_uppercase)
            elif i == "@":
                password += random.choice(string.ascii_lowercase)
            elif i == "#":
                password += random.choice(string.digits)
            elif i == "$":
                password += random.choice(string.punctuation)
            else:
                password += i

        return password

    def copySelectedToClipboard(self):
        """Sends selected rows to clipboard as tab-separated text"""
        self.tableLogins.selectAll()
        rows = utilities.get_selected_rows_from_qtablewidget(self.tableLogins)
        strings = []
        for row in rows:
            textRow = []
            for item in row:
                textRow += [item.text()]
            strings += ["\t".join(textRow)]
        result = "\n".join(strings)
        self.clip.setText(result)

def unhandled_exception(exc_type, exc_value, exc_traceback):
    logger.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    sys.exit(1)

def main():
    sys.excepthook = unhandled_exception

    QtCore.QCoreApplication.setApplicationName(__appname__)
    QtCore.QCoreApplication.setApplicationVersion(str(__version__))

    app = QtWidgets.QApplication(sys.argv)
    form = Main()

    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
