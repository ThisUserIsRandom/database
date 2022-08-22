from os import path
import makeDB
from time import sleep
import importlib


def selectDatabase():
    global selectedDataBase
    enterDbName = input("select Database[hit enter to skip] :")
    if path.isdir('databases/'+enterDbName) == True:
        selectedDataBase = enterDbName
        return enterDbName
    else:
        print("[-] this database doesn't exist \n")
        print('[?] to make a database enter query: create db ')
        DatabaseQuery = input(f"database:[] > ")
        if DatabaseQuery == 'create db':
            makeDB.madeDB()
        else:
            selectDatabase()

# subprocess.call(['py','makeDB.py'])
selectedDataBase = selectDatabase()
def wholeProcess():
    print('='*15+' Welcome '+'='*15)
    print('[+] Some basic queries \n [+] create db : to make a database \n [+] create table : to make a table \n [+] enter data : to enter data in table \n [+] quit : to close session \n [+] select db : to select database')
    while True:
        try:
            print('')
            DatabaseQuery = input(f"database:[{selectedDataBase}] > ")
            if DatabaseQuery == 'create db':
                # Dbname = makeDB.selectDataBaseName()
                makeDB.madeDB()
            elif DatabaseQuery == 'create table': 
                def check_database():
                    if selectedDataBase == '':
                        selectDatabase()
                    else:
                        from makeTable import makeDatabase , maketable , makeScheme,makeSchemeList
                        cache_Scheme = makeDatabase()
                        temptableName = cache_Scheme[0]
                        tempColumns = cache_Scheme[1]
                        try:
                            maketable(selectedDataBase,temptableName,cache_Scheme[1],Scheme=makeScheme(makeSchemeList(tempColumns),temptableName))
                        except Exception as e:
                            print("select correct Database",e)
                            selectDatabase()
                check_database()
            elif DatabaseQuery == 'quit':
                print("[-] closing session")
                exit()
            elif DatabaseQuery == 'select db':
                selectDatabase()
            elif DatabaseQuery == 'enter data':
                import putData
                tableName = input("[+]Enter tableName :")
                try:
                    putData.insertData(selectedDataBase,tableName)
                except:
                    print("[-]Database or table name is wrong , please check database , tableName \n")
            elif DatabaseQuery == 'show data':
                tableName = input("[+]Enter tableName :")
                import pullData
                try:
                    pullData.makeLiteralTable(selectedDataBase,tableName)
                except:
                    print("[-]Database or table name is wrong")
        except KeyboardInterrupt:
            print("[-] session terminated")
            wholeProcess() 
wholeProcess()