from dataclasses import dataclass
from os import path
import makeDB
import showdbtab
import deleteData

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
    print('\n[+] show data : to see data from tables \n[+] delete from table_name : to delete a row in a table \n[+] delete table : to delete table \n[+] delete database : to delete database')
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
                column = input("[+] column name to enter , seperate by ',' (enter * for all) :")
                import pullData
                try:
                    pullData.makeLiteralTable(selectedDataBase,tableName,column.split(',')) 
                except:
                    print("[-]Database or table or column name is wrong ")
            elif DatabaseQuery == 'show db':
                showdbtab.askInput('DB','')
            elif DatabaseQuery == 'show tables':
                showdbtab.askInput('files',selectedDataBase)

            elif DatabaseQuery.split(' ')[0] == 'delete' :
                queryList = DatabaseQuery.split(' ')
                if len(queryList) == 3:
                    try:
                        tableName = queryList[2]
                        # print(selectDatabase,tableName)
                        print("[+] Enter info regarding entry you want to delete :")
                        condition = input("[+] Enter a condition(like :- id=1) seperated by '=' :")
                        conditionColumnName = condition.split('=')[0]
                        conditionValue = condition.split('=')[1] 
                        deleteData.deleteEntry(selectedDataBase,tableName,conditionColumnName,conditionValue)
                    except Exception as e:
                        print(f"[-]Something went wrong =>{e}")
                        wholeProcess()
                elif len(queryList) == 2:
                    if queryList[1] == 'db':
                        try:
                            deleteData.deleteDB(selectedDataBase)
                        except:
                            print(f'[-] Database not found!')
                    elif queryList[1] == 'table':
                        tableName = input(f"[+]Enter table name to delete")
                        deleteData.deletetable(selectedDataBase,tableName)
                else:
                    print('[-] Delete what!')
                    wholeProcess()
                    
                            
        except KeyboardInterrupt:
            print("[-] session terminated")
            wholeProcess() 
wholeProcess()