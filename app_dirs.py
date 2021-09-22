import appdirs
import os
import sys

class AppDirs():

    def __init__(self, appname, isportable=False, portabledatadirname='data'):
        self.isportable = isportable
        self.portabledatadirname = portabledatadirname
        self.appname = appname

    def get_appdir(self):
        # get path of program dir.
        # sys._MEIPASS - variable of pyinstaller (one-dir package) with path to executable
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            #pyinstaller detected!
            appdir = sys._MEIPASS
        else:
            #not pyinstaller
            appdir = os.path.dirname(os.path.abspath(__file__))
        return appdir

    def get_datadir(self):
        appdir = self.get_appdir()
        if self.isportable:
            datadir = os.path.join(appdir, self.portabledatadirname)
        else:
            datadir = appdirs.user_config_dir(self.appname, False)

        try:
            os.makedirs(datadir, exist_ok=True)
        except Exception as e:
            print(e)
        else:
            return datadir

    def get_file(self, filename):
        datadir = self.get_datadir()
        file = os.path.join(datadir, filename)
        if os.path.isfile(file):
            return file
        else:
            try:
                with open(file, 'w') as f:
                    f.write('')
            except Exception as e:
                print(e)
            else:
                return file