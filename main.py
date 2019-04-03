import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets


import logging
import os
#from pyad import pyad
#import pyad.adquery
import random
import regex
import string
import sys

import utilities

from ui_files import pyMain


__appname__ = "RussianFIO2AD"
__version__ = "0.0.1"


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


class Main(QtWidgets.QDialog, pyMain.Ui_Dialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.clip = QtGui.QClipboard()
        self.adTree.itemClicked.connect(self.adTreeItemClicked)
        self.pasteFIO.clicked.connect(self.pasteFIOClicked)
        self.genLogins.clicked.connect(self.genLoginsClicked)
        self.copyLogins.clicked.connect(self.copySelectedToClipboard)

        self.createAccounts.clicked.connect(self.createADAccounts)

        #adOUs = self.get_ad_tree()
        adOUs = ["asd\\asdqw", "wqe\\qweqe", "asd\\123ew", "asd\\123ew\\234"]
        list = self.tree_widget_list(adOUs)
        self.adTree.insertTopLevelItems(0, list)


    def adTreeItemClicked(self):
        item = self.adTree.selectedItems()
        if item:
            self.createAccounts.setEnabled(True)
            selectedText = item[0].text(0)

            parents = []
            for index in self.adTree.selectedIndexes():
                while index.parent().isValid():
                    index = index.parent()
                    parents = [index.sibling(index.row(), 0).data()] + parents


            self.adPath = "/".join(parents + [selectedText])
            self.adTree.setHeaderLabel(self.adPath)

    def createADAccounts(self):
        if self.adPath:
            for i in range(0, self.loginsTable.rowCount()):

                displayName = self.loginsTable.item(i, 0).text()
                login = self.loginsTable.item(i, 1).text()
                password = self.loginsTable.item(i, 2).text()

                self.logBrowser.append("""===================\nCreating in "{}"\n===================""".format(self.adPath))
                self.logBrowser.append("""{}: {}, {} """.format(displayName, login, password))


    def get_ad_tree(self):
        query = pyad.adquery.ADQuery()

        query.execute_query(
            attributes=["distinguishedName", "description"],
            where_clause="objectClass = 'organizationalUnit'"
            )
        ous = []
        for row in query.get_results():
            path = row["distinguishedName"].replace(",OU=", "\\").replace("OU=","")
            path = path.split("\\")
            path = reversed(path)
            path = "\\".join(path)
            ous += [path]
        return ous

    def tree_widget_list(self, show_list):
        """
        Creates a list for updating tree widget
        :param show_list:
        :return:
        """
        items = []
        for item in show_list:
            item_parts = item.split('\\')

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

    def pasteFIOClicked(self):
        """Fills FIO table from clipboard"""
        clipboard = self.clip.text().splitlines()
        self.namesTable.setRowCount(0)

        for fio in clipboard:
            try:
                fioSplitted = self.split_fio(fio)
            except:
                pass
            else:
                row = self.namesTable.rowCount()
                self.namesTable.insertRow(row)

                for n in range(1, len(fioSplitted)+1):
                    t = fioSplitted[n-1].strip()
                    self.namesTable.setItem(row, n-1, QtWidgets.QTableWidgetItem(t))

    def genLoginsClicked(self):
        self.loginsTable.setRowCount(0)
        for fioRow in range(0, self.namesTable.rowCount()):
            row = self.loginsTable.rowCount()
            self.loginsTable.insertRow(row)

            f = self.namesTable.item(fioRow, 0).text()
            i = self.namesTable.item(fioRow, 1).text()
            o = self.namesTable.item(fioRow, 2).text()
            fio = "{} {} {}".format(f,i,o)
            password = (random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + str(random.randint(0,9))
                        + str(random.randint(0, 9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
                        + str(random.randint(0, 9))
                        )

            login = self.login_templating(f,i,o)

            self.loginsTable.setItem(row, 0, QtWidgets.QTableWidgetItem(fio))
            self.loginsTable.setItem(row, 1, QtWidgets.QTableWidgetItem(login))
            self.loginsTable.setItem(row, 2, QtWidgets.QTableWidgetItem(password))



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


    def copySelectedToClipboard(self):
        """Sends selected rows to clipboard as tab-separated text"""
        rows = utilities.get_selected_rows_from_qtablewidget(self.loginsTable)
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
