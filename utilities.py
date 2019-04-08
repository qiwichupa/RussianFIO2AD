from pyad import pyad

def str2bool(arg):
    return(str(arg).lower() in ["true", "0", "ok"])

def bool2str(arg):
    if arg:
        return("True")
    else:
        return("False")

def mysql_query_wildficator(query):
    wild_query = query.replace("%", "\%").replace("_", "\_").replace("*", "%").replace("?", "_")
    return(wild_query)

def mysql_index_is_exists(connection, tablename, index):
    sql = "SHOW KEYS FROM  " + tablename + "  WHERE Key_name = %s"
    cursor = connection.cursor()
    cursor.execute(sql, (index,))
    check = cursor.fetchall()
    if check:
        return(True)
    else:
        return(False)

def sql_search_result_iterator(cursor, chunkSize=1000):
    while True:
        results = cursor.fetchmany(chunkSize)
        if not results:
            break
        for result in results:
            yield result

def scantree(path):
    """Recursively yield DirEntry objects for given directory.
    Usage:
    for entry in scantree(path):
        print(entry.path)
    """
    from os import scandir
    for entry in scandir(path):
        if entry.is_dir(follow_symlinks=False):
            try:
                #yield entry
                yield from scantree(entry.path)
            except Exception as e:
                print(str(e))
        elif entry.is_file():
            try:
                yield entry
            except Exception as e:
                print(str(e))
        else:
            pass

def get_extension_from_filename(name):
    return(name[name.rfind(".") + 1:] if name.rfind(".") != -1 else "")

def get_humanized_size(num, suffix='B'):
    num = float(num)
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return("%.1f%s%s" % (num, 'Yi', suffix))

def get_selected_rows_from_qtablewidget(qTableWidget, sortByColumn=0):
    indexes = qTableWidget.selectionModel().selectedRows(sortByColumn)
    rows = []
    for index in sorted(indexes):
        item = qTableWidget.itemFromIndex(index)
        row = qTableWidget.row(item)
        rowItems = []
        for column in range(0, qTableWidget.columnCount()):
            rowItems += [qTableWidget.item(row, column)]
        rows += [rowItems]
    return(rows)

class LoggerWriter:
    def __init__(self, level):
        # self.level is really like using log.debug(message)
        # at least in my case
        self.level = level

    def write(self, message):
        # if statement reduces the amount of newlines that are
        # printed to the logger
        if message != '\n':
            self.level(message)

    def flush(self):
        # create a flush method so things can be flushed when
        # the system wants to. Not sure if simply 'printing'
        # sys.stderr is the correct way to do it, but it seemed
        # to work properly for me.
        #self.level(sys.stderr)
        pass

def translit(string):
    """ This function works just fine """
    capital_letters = {
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'E',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Sch',
        'Ъ': '',
        'Ы': 'Y',
        'Ь': '',
        'Э': 'E',
        'Ю': 'Yu',
        'Я': 'Ya'
    }

    lower_case_letters = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'e',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sch',
        'ъ': '',
        'ы': 'y',
        'ь': '',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya'
    }

    translit_string = ""

    for index, char in enumerate(string):
        if char in lower_case_letters.keys():
            char = lower_case_letters[char]
        elif char in capital_letters.keys():
            char = capital_letters[char]
            if len(string) > index+1:
                if string[index+1] not in lower_case_letters.keys():
                    char = char.upper()
            else:
                char = char.upper()
        translit_string += char

    return translit_string

def get_container_from_dn(dn, rootcontainer=None):
    if rootcontainer is None:
        rootcontainer = pyad.adcontainer.ADContainer.from_dn(pyad.adcontainer.ADContainer.default_domain)

    try:
        currentdn = rootcontainer.dn
    except:
        pass
    else:
        if dn == currentdn:
            return rootcontainer

    try:
        children = rootcontainer.get_children(filter_=[pyad.adcontainer.ADContainer])
    except:
        return None

    for c in children:
        if c.dn in dn:
            try:
                container = get_container_from_dn(dn, rootcontainer=c)
                if container is not None:
                    return container
            except:
                pass

