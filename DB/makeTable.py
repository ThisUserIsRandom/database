from os import path 
import importlib

def check_database(selectedDatabase):
    isExist = path.isdir(f'databases/{selectedDatabase}')
    if isExist == True:
        return selectedDatabase
    else:
        print("[-] not database from this name")
        exit()

# if __name__ == 'main':
def makeDatabase():
    databaseColumn = 1
    dataBaseName = input("[+] Enter name of table to make :") 
    try:
        databaseColumn = int(input("[+] Enter number of column to make :"))
    except:
        print("[-]input can only be integer")
        makeDatabase()
    Scheme = {}
    for data in range(0,databaseColumn):
        columnName = input(f'[+] enter name of column no.{data+1} :')
        while True:
            possibleOutputs = (0,1) 
            try:
                PrimaryKeyInput = int(input('[+] Is this column contain primary key (0 for no , 1 for yes) :'))
            except:
                print("[-]input can only be integer")
            if PrimaryKeyInput not in possibleOutputs:
                continue
            else:
                PrimaryKeyInput = PrimaryKeyInput
                break;False
        while True:
            possibleOutputs = ('str','int')
            DataTypeColumn = input(f'[+] Enter datatype of {possibleOutputs} :')
            if DataTypeColumn not in possibleOutputs:
                print("[+] none entered default= string ")
                DataTypeColumn = 'str'
                break;False
            else:
                break;False
        tempdict = {f'{columnName}':[PrimaryKeyInput,DataTypeColumn]}
        Scheme.update(tempdict)
        print('-'*40)
    return [ dataBaseName, Scheme]

# tempdatabaseName = check_database()
def choosedbName(nameoftable):
    try:
        config = importlib.import_module(
            f'{nameoftable}', package='mypackage')
        return config
    except:
        return 'library not found'

# makeTable(tempdatabaseName,temptableName,cache_scheme[1],Scheme=makeScheme(makeSchemeList(tempcolumns))) 
def maketable(databaseName, tableName, cacheScheme,Scheme):
    try:
        filecacheOpen = open( f'databases/{databaseName}/cache_{tableName}.py', 'w')
        filecacheOpen.write(f'{tableName}={cacheScheme}')
        filecacheOpen.close()
        fileOpen = open(f'databases/{databaseName}/{tableName}.py', 'w')
        fileOpen.write(f'{tableName}={Scheme}')
        fileOpen.close()
    except Exception as e:
        print(e)
    print(f'''New Table in {databaseName} formed by name {tableName}  with Scheme => {Scheme}''')
# cache_scheme = makeDatabase() 
# global tempcolumns
# tempcolumns = list(cache_scheme[1])
# temptableName = cache_scheme[0]
def makeSchemeList(columns):
    listofstuff = []
    for attribute in columns:
        listofstuff.append(attribute)
    return listofstuff
def makeScheme(SchemeList,temptableName):
    tempdirmain = {} 
    tempDir = {}
    firstentry = {f'{temptableName}_0':{}}
    for stuff in SchemeList:
        tempDirupdate = {f'{stuff}': {}}
        tempDir.update(tempDirupdate)
    firstentry[f'{temptableName}_0'] = tempDir
    tempdirmain.update(firstentry) 
    return tempdirmain
