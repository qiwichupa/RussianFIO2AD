import PySide2.QtCore as QtCore
import PySide2.QtGui as QtGui
import PySide2.QtWidgets as QtWidgets


import logging
import os
import pyperclip
#import pyad
import sys

import utilities

from ui_files import pyMain


__appname__ = "QT-FIO2AD"
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
sys.stdout = utilities.LoggerWriter(logger.warning)
sys.stderr = utilities.LoggerWriter(logger.warning)
try:
    removedLogFileSize
    logger.info("Previous logfile was removed by size limit (" + str(logFileSizeLimit) + "MB). Size was: " + str(removedLogFileSize) + " bytes.")
except:
    pass


class Main(QtWidgets.QMainWindow, pyMain.Ui_Dialog):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.clip = QtGui.QClipboard()

        self.pasteFIO.clicked.connect(self.pasteFIOClicked)

    def pasteFIOClicked(self):
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

                numItem = QtWidgets.QTableWidgetItem()
                numItem.setData(QtCore.Qt.EditRole, row + 1)
                self.namesTable.setItem(row, 0, numItem)
                for n in range(1, len(fioSplitted)+1):
                    t = fioSplitted[n-1].strip()
                    self.namesTable.setItem(row, n, QtWidgets.QTableWidgetItem(t))



    def split_fio(self, fio):
        result = fio.strip().split("\t", maxsplit=3)
        if len(result) > 1:
            return result


        result = fio.strip().split(" ", maxsplit=3)
        if len(result) > 1:
            return result

        raise Exception


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