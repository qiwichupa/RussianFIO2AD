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
from app_dirs import AppDirs

from ui_files import main


class Main(QtWidgets.QMainWindow, main.Ui_MainWindow):

    commonAttributes = {}
    groups = {}

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.setWindowTitle(__appname__ + " (v. " + __version__ + ")")
        self.configfile = os.path.join(appDataPath, "settings.ini")
        self.settings = QtCore.QSettings(self.configfile, QtCore.QSettings.IniFormat)
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
        self.buttonTestAccounts.clicked.connect(self.testADAccounts)
        self.buttonCreateAccounts.clicked.connect(self.createADAccounts)

        self.buttonConnectToAD.hide()
        self.adServer.hide()
        self.adUser.hide()
        self.adPassword.hide()

        self.initSettings()
        self.loadAdToUI()

    def initSettings(self):
        """Инициализация настроек, вызов заполнения дерева AD и списка групп"""
        if not self.settings.value("templLogin"):
            self.settings.setValue("templLogin", "f_i1o1")
        if not self.settings.value("templPassword"):
            self.settings.setValue("templPassword", "!@######$")
        if not self.settings.value("commonAttributes"):
            self.settings.setValue("commonAttributes", "description,company,department")
        if not self.settings.value("favoriteGroups"):
            self.settings.setValue("favoriteGroups", "")

        for key in self.settings.value("commonAttributes").split(","):
            self.commonAttributes[key] = ""
            self.comboBoxAttributes.addItems([key])

        self.favoriteGroups = self.settings.value("favoriteGroups").split(",")

        self.loginTemplate.setText(self.settings.value("templLogin"))
        self.passwordMask.setText(self.settings.value("templPassword"))
        self.logBrowser.append("""Загружен конфиг: {cfg}""".format(cfg=self.configfile))

    def refreshADGroups(self):
        """Обновление списка групп"""
        try:
            q = pyad.adquery.ADQuery()
            q.execute_query(
                attributes=["distinguishedName", "cn"],
                where_clause="objectClass = 'group'"
                )
        except Exception as e:
            self.logBrowser.append("""Ошибка получения групп: {}""".format(str(e)))
            logger.warning("""Ошибка получения групп: {}""".format(str(e)))
            self.groups["Ошибка"] = [False, False]
            self.comboboxGroups.setDisabled(True)
            self.checkboxAddToGroup.setDisabled(True)
        else:
            self.groups = {}
            for group in q.get_results():
                if "\\" not in group["distinguishedName"]:
                    cn = group["cn"]
                    dn = group["distinguishedName"]
                    self.groups[cn] = [dn, False]
        finally:
            self.refreshComboboxGroups()

    def comboboxGroupsActivated(self):
        """Установка чекбокса в соответствии с тем - выбрано
        добавление в эту группу создаваемой учетной записи или нет"""
        cn = self.comboboxGroups.currentText()
        self.checkboxAddToGroup.setChecked(self.groups[cn][1])

    def checkboxAddToGroupStateChanged(self):
        """Добавляет или убирает группу в список групп, в которые
        будет добавлена учетная запись, после чего обновляет self.comboboxGroups"""
        currentCN = self.comboboxGroups.currentText()
        if self.checkboxAddToGroup.isChecked():
            self.groups[currentCN][1] = True
        else:
            self.groups[currentCN][1] = False

        self.refreshComboboxGroups()
        self.comboboxGroups.setCurrentText(currentCN)

    def refreshComboboxGroups(self):
        """Обновляет self.comboboxGroups с учетом статуса групп (выбрана или
        не выбрана группа для добавления в нее учетной записи)"""
        self.comboboxGroups.clear()
        n = 0
        # первыми в список - отмеченные
        for cn in sorted(self.groups.keys(), key=str.lower):
            if self.groups[cn][1] is True:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/icons/icons/edited.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.comboboxGroups.addItem(cn)
                self.comboboxGroups.setItemIcon(n, icon)
                n += 1
        # вторыми в список - из списка избранного (favoriteGroups из файла настроек)
        for cn in sorted(self.groups.keys(), key=str.lower):
            if self.groups[cn][1] is False and cn in self.favoriteGroups:
                self.comboboxGroups.addItem(cn)
        # далее - все остальные
        for cn in sorted(self.groups.keys(), key=str.lower):
            if self.groups[cn][1] is False and cn not in self.favoriteGroups:
                self.comboboxGroups.addItem(cn)

    def lineEditAttributeEmitted(self):
        """Изменяет значение переменной аттрибута, помечает не пустые элементы self.lineEditAttribute"""
        key = self.comboBoxAttributes.currentText()
        self.commonAttributes[key] = self.lineEditAttribute.text().strip()
        if self.lineEditAttribute.text().strip() != "":
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(":/icons/icons/edited.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:
            icon = QtGui.QIcon()
        self.comboBoxAttributes.setItemIcon(self.comboBoxAttributes.currentIndex(), icon)

    def loginTemplateEmitted(self):
        """Сохраняет в конфиг значение шаблона логина"""
        self.settings.setValue("templLogin", self.loginTemplate.text())

    def passwordMaskEmitted(self):
        """Сохраняет в конфиг значение шаблона пароля"""
        self.settings.setValue("templPassword", self.passwordMask.text())

    def comboBoxAttributesActivated(self):
        """Сохраняет значение аттрибута в словарь с индексом аттрибута"""
        key = self.comboBoxAttributes.currentText()
        self.lineEditAttribute.setText(self.commonAttributes[key])

    def buttonConnectToADClicked(self):
        pass

    def loadAdToUI(self):
        """Пытается получить дерево AD, в случае успеха отрисовывает
        его в виджете и вызывает обновление списка групп"""
        try:
            adOUs = self.get_ad_tree()
        except Exception as e:
            self.logBrowser.append("""Ошибка получения дерева AD: {}""".format(str(e)))
            logger.warning("""Ошибка получения дерева AD: {}""".format(str(e)))
        else:
            list = self.tree_widget_list(adOUs)
            self.adTree.insertTopLevelItems(0, list)
        finally:
            self.refreshADGroups()

    def adTreeItemClicked(self):
        """Создает self.adPathList из элементов DistinguishedName выбранной OU"""
        item = self.adTree.selectedItems()
        if item:
            self.buttonTestAccounts.setEnabled(True)
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
        """Для каждого элемента списка логинов запускает функцию создания учетной записи.
        Обратить внимание: container - объект OU, получается при помощи самописной функции,
        потому что штатная (pyad.adcontainer.ADContainer.from_dn) выдает исключение,
        если в Distinguished Name встречаются экранированные символы (баг pyad)"""
        self.buttonTestAccounts.setDisabled(True)
        self.buttonCreateAccounts.setDisabled(True)
        if self.adPathList:
            domain = "DC=" + ",DC=".join(self.domainList)
            organizationUnitDN = "OU=" + ",OU=".join(self.adPathList) + "," + domain
            container = utilities.get_container_from_dn(organizationUnitDN)

            self.logBrowser.append("""===================\nСоздание в "{}"\n===================""".format("/".join(self.adPathListReversed)))
            logger.info("""\n===================\nСоздание в "{}"\n===================""".format("/".join(self.adPathListReversed)))
            # users = []
            for i in range(0, self.tableLogins.rowCount()):

                displayName = self.tableLogins.item(i, 0).text().strip()
                login = self.tableLogins.item(i, 1).text().strip()
                password = self.tableLogins.item(i, 2).text().strip()

                if displayName != "" and login != "" and password != "":
                    # users += [{"displayName": displayName, "login": login, "password": password}]
                    self.add_user_to_ad(displayName, login, password, container)
                else:
                    self.logBrowser.append("\nПропуск: {} {} {} - пустое поле\n".format(displayName, login, password))

            self.buttonTestAccounts.setEnabled(True)
            self.buttonCreateAccounts.setEnabled(True)

    def testADAccounts(self):
        """ Для каждого элемента списка логинов проверяет наличие в AD логина или Common Name"""
        for row in range(0, self.tableLogins.rowCount()):
            utilities.set_bgcolor_qt_row(self.tableLogins, row, QtGui.QColor(255, 255, 255))

        if self.adPathList:
            domain = "DC=" + ",DC=".join(self.domainList)
            organizationUnitDN = "OU=" + ",OU=".join(self.adPathList) + "," + domain

            self.logBrowser.clear()
            self.logBrowser.append("""===================\nПроверка учетных записей\n===================""")
            for i in range(0, self.tableLogins.rowCount()):
                displayName = self.tableLogins.item(i, 0).text().strip()
                login = self.tableLogins.item(i, 1).text().strip()
                password = self.tableLogins.item(i, 2).text().strip()

                if displayName != "" and login != "" and password != "":
                    self.test_user_in_ad(i+1, displayName, login, organizationUnitDN, domain)
                else:
                    self.logBrowser.append("\nПропуск: {} {} - пустое поле\n".format(displayName, login))
            self.logBrowser.append("""Проверка учетных записей завершена\n""")

    def add_user_to_ad(self, displayName, login, password, container):
        """Создает учетную запись.
        Пояснение: учетная запись может быть создана с ошибкой и вызвать этим исключение.
        Типичный пример - попытка создания с указанием пароля, не соответствующего
        политике паролей. Поэтому при возникновении исключения я пробую удалить возможно
        созданную учетную запись (она НЕ будет создана при наличии в домене учетной записи  с таким же DN
        или логином). """
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
            user = pyad.aduser.ADUser.create(displayName, container, optional_attributes=attributes)
            user.set_password(password=password)
        except Exception as e:
            self.logBrowser.append("""\n<b>Ошибка</b>: {}({}: {})\n """.format(str(e), displayName, login))
            logger.warning("""Ошибка: {}({}: {}, {}) """.format(str(e), displayName, login, str(container)))
            try:
                # не user.remove() потому что он падает, если OU содержит экранированные символы в DN
                container.remove_child(user)
                logger.info("Удален: CN={},{}".format(displayName, container.dn))
            except Exception as e:
                logger.info("Ошибка удаления: {} \nCN={},{}".format(str(e), displayName, container.dn))

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
                if self.groups[cn][1]:
                    try:
                        logger.info("""Получение объекта группы: {}""".format(self.groups[cn][0]))
                        group = pyad.adgroup.ADGroup.from_dn(self.groups[cn][0])
                        print(str(group))
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

    def test_user_in_ad(self, stringNum, displayName, login,  organizationUnitDN, domain):
        """Проверяет учетную запись на существование в AD логина (sAMAccountName) или distinguishedName. """
        q = pyad.adquery.ADQuery()

        # Поиск повторяющихся distinguishedName
        q.execute_query(
            attributes=["distinguishedName", "sAMAccountName"],
            where_clause="displayName = '{}'".format(displayName),
            base_dn=organizationUnitDN
            )
        dnameDoublesList = []
        for row in q.get_results():
            pathList = row["distinguishedName"].replace("CN={},OU=".format(displayName), "").replace(",{}".format(domain), "").split(",OU=")
            path = "<b>/</b>".join(list(reversed(pathList)))
            dnameDoublesList.append(""""{}"  (Логин: "{}")""".format(path, row["sAMAccountName"]))

        # Поиск повторяющихся логинов (sAMAccountName)
        q.execute_query(
            attributes=["distinguishedName", "sAMAccountName"],
            where_clause="sAMAccountName = '{}'".format(login),
            base_dn=domain
            )
        samnameDoublesList = []
        for row in q.get_results():
            pathList = row["distinguishedName"].replace("CN={},OU=".format(displayName), "").replace(",{}".format(domain), "").split(",OU=")
            path = "<b>/</b>".join(list(reversed(pathList)))
            samnameDoublesList.append(""""{}"  (Логин: "{}")""".format(path, row["sAMAccountName"]))

        # Запись лога ошибок
        if len(dnameDoublesList) > 0 or len(samnameDoublesList) > 0:
            utilities.set_bgcolor_qt_row(self.tableLogins, stringNum - 1, QtGui.QColor(255, 230, 230))
            self.logBrowser.append("#{}. <b>{}</b>".format(stringNum, displayName))
            if len(dnameDoublesList) > 0:
                self.tableLogins.item(stringNum - 1, 0).setBackground(QtGui.QColor(255, 161, 137))
                self.logBrowser.append("<u>Cовпадение distinguishedName в OU</u>:".format(displayName))
                for dname in dnameDoublesList:
                    self.logBrowser.append(dname)
            if len(samnameDoublesList) > 0:
                self.tableLogins.item(stringNum - 1, 1).setBackground(QtGui.QColor(255, 161, 137))
                self.logBrowser.append("<u>Cовпадение логина (sAMAccountName) в OU</u>:".format(displayName))
                for samname in samnameDoublesList:
                    self.logBrowser.append(samname)
            self.logBrowser.append("")

    def get_ad_tree(self):
        """Запрашивает из AD distinguishedName для всех UO,
        возвращает список из списков элементов DN"""
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

                while domain is False:
                    self.domainList = row["distinguishedName"].split(",DC=", maxsplit=1)[1].split(",DC=")
                    domain = ".".join(self.domainList)
                    self.logBrowser.append("Подключено к домену: {}".format(domain))
                pathList = regex.subf("^OU=", "", row["distinguishedName"].split(",DC=")[0]).split(",OU=")
                reversedPathList = list(reversed(pathList))
                ous += [reversedPathList]
            return sorted(ous)

    def tree_widget_list(self, show_list):
        """Создает список для обновления дерева AD"""
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
        """Вставляет список фамилий (замещая или дополняя список виджета)"""
        clipboard = self.clip.text().splitlines()

        row = 0
        for f in clipboard:
            f = f.strip()
            if row >= self.tableNames.rowCount():
                self.tableNames.insertRow(row)
            self.tableNames.setItem(row, 0, QtWidgets.QTableWidgetItem(f))
            row += 1

    def buttonPasteIClicked(self):
        """Вставляет список имен (замещая или дополняя список виджета)"""
        clipboard = self.clip.text().splitlines()

        row = 0
        for f in clipboard:
            f = f.strip()
            if row >= self.tableNames.rowCount():
                self.tableNames.insertRow(row)
            self.tableNames.setItem(row, 1, QtWidgets.QTableWidgetItem(f))
            row += 1

    def buttonPasteOClicked(self):
        """Вставляет список отчеств (замещая или дополняя список виджета)"""
        clipboard = self.clip.text().splitlines()

        row = 0
        for f in clipboard:
            f = f.strip()
            if row >= self.tableNames.rowCount():
                self.tableNames.insertRow(row)
            self.tableNames.setItem(row, 2, QtWidgets.QTableWidgetItem(f))
            row += 1

    def buttonPasteFIOClicked(self):
        """Вставляет список ФИО (обновляя список виджета)"""
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
        """Генерирует список логинов из списка ФИО"""
        self.tableLogins.setRowCount(0)
        for fioRow in range(0, self.tableNames.rowCount()):
            row = self.tableLogins.rowCount()
            self.tableLogins.insertRow(row)

            fNone = iNone = oNone = False
            f = i = o = ""

            try:
                f = self.tableNames.item(fioRow, 0).text().strip()
                if len(f) == 0: fNone = True
            except Exception as e:
                fNone = True
            try:
                i = self.tableNames.item(fioRow, 1).text().strip()
                if len(i) == 0: iNone = True
            except Exception as e:
                iNone = True
            try:
                o = self.tableNames.item(fioRow, 2).text().strip()
                if len(o) == 0: oNone = True
            except Exception as e:
                oNone = True

            fio = "{} {} {}".format(f, i, o).replace("  ", " ").strip()
            password = self.password_templating()

            login = self.login_templating(f, i, o)[:20]

            self.tableLogins.setItem(row, 0, QtWidgets.QTableWidgetItem(fio))
            self.tableLogins.setItem(row, 1, QtWidgets.QTableWidgetItem(login))
            self.tableLogins.setItem(row, 2, QtWidgets.QTableWidgetItem(password))

            if fNone or iNone or oNone: self.tableLogins.item(row, 0).setBackground(QtGui.QColor(255, 255, 155))
            if fNone: self.logBrowser.append("Некритично: строка {} - отсутствует фамилия".format(row + 1))
            if iNone: self.logBrowser.append("Некритично: строка {} - отсутствует имя".format(row + 1))
            if oNone: self.logBrowser.append("Некритично: строка {} - отсутствует отчество".format(row + 1))

    def split_fio(self, fio):
        """Возвращает разделенные ФИО,
        разделение по табуляции (для вставки из таблицы) или пробелу.
        Если ФИО не разделилось хотя бы на 2 части - вызывает исключение"""
        result = fio.strip().split(None, maxsplit=2)
        if len(result) > 1:
            return result

        raise Exception

    def login_templating(self, f, i, o):
        """Генерирует и возвращает логин из ФИО по шаблону"""
        fLat = utilities.translit(f)
        iLat = utilities.translit(i)
        oLat = utilities.translit(o)
        template = self.loginTemplate.text()

        template = regex.subf(r'([fio])(\d*)', '{{{1}:.{2}}}', template)
        template = template.replace(":.}", "}")

        login = self.loginPrefix.text() + template.format(f=fLat, i=iLat, o=oLat)

        return login

    def password_templating(self):
        """Генерирует и возвращает пароль по шаблону"""
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
        """Копирует список учетных записей в буфер обмена как текст, разделенный табуляцией"""
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
    __appname__ = "RussianFIO2AD"
    __version__ = "0.1.1"

    # set working directory
    appdirs = AppDirs(__appname__, isportable=True, portabledatadirname='data')
    appDataPath = appdirs.get_datadir()
    logfile = os.path.join(appDataPath, __appname__ + ".log")

    # remove large logfile
    logFileSizeLimit = 1  # MB
    try:
        os.stat(logfile).st_size
        if os.stat(logfile).st_size > logFileSizeLimit * 1024 ** 2:
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
    # sys.stdout = utilities.LoggerWriter(logger.warning)
    sys.stderr = utilities.LoggerWriter(logger.warning)
    try:
        removedLogFileSize
        logger.info("Previous logfile was removed by size limit (" + str(logFileSizeLimit) + "MB). Size was: " + str(removedLogFileSize) + " bytes.")
    except:
        pass

    main()
