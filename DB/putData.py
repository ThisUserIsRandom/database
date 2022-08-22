from importlib import import_module
from os import path

def check_database():
    selectedDatabase = input('[+] Name of Database :')
    isExist = path.isdir(f'databases/{selectedDatabase}')
    if isExist == True:
        return selectedDatabase
    else:
        print("[-] not database from this name")
        exit()
# tempDB = input('database name:')
# tableName = input('table name :')

def checkPrimary(dictionary,column,enterData,uniquesStatus):
    tempList = []
    if uniquesStatus == 1:
        allEntries = list(dictionary)
        for entry in allEntries:
            tempList.append(dictionary[entry][column])
            def checkIfDuplicates(listOfElems):
                if enterData in listOfElems:
                    return True
                else:
                    return False
        # print(checkIfDuplicates(tempList))
        if checkIfDuplicates(tempList) == True: 
            return False
        else:
            return True
    else:
        return True

def importTableCache(DatabaseName,tableName):
    cacheFile = import_module(f"databases.{DatabaseName}.{tableName}")
    return  cacheFile

def importTable(DatabaseName,tableName):
    mainFile = import_module(f'databases.{DatabaseName}.{tableName}')
    return mainFile

def insertData(DatabaseName,tableName):#,DataToInsert
    tempTableName = 'cache_'+tableName
    tableData = import_module(f"databases.{DatabaseName}.{tableName}")
    cacheSchemeData = import_module(f"databases.{DatabaseName}.cache_{tableName}") 
    tempinstanceData = tableData.__dict__.get(f'{tableName}') 
    schemeDataList = list(cacheSchemeData.__dict__.get(f'{tableName}'))
    try:
        tableTamplate = list(tempinstanceData)[0]
    except:
        tableTamplate = f'{tableName}_0'
    Data = tempinstanceData[tableTamplate] 
    def verifyData(Data):
        newformedDict = {}
        ListData = list(Data)
        tempListTostorevalues = []
        for item in ListData: 
            requirements = cacheSchemeData.__dict__.get(f'{tableName}') 
            IsPrimaryKey = requirements[item][0]
            Datatype = requirements[item][1] 
            # print(IsPrimaryKey,Datatype)
            shouldInsert = []
            if Datatype == 'str':
                shouldInsert.append(True) 
                enterData = input(f'enter {item} :')
            else:
                try:
                    enterData = int(input(f'enter {item} :'))
                    shouldInsert.append(True)
                except:
                    print("data cannot be string in this colum ")
                    exit()
            shouldInsert.append(checkPrimary(tempinstanceData,item,enterData,IsPrimaryKey))
            # print(shouldInsert)
            if shouldInsert[0] == True and shouldInsert[1] == True:
                tempListTostorevalues.append(enterData)
            else:
                print('[+] Some error occured')
                exit()
        i = 0
        for item in ListData:# ListData will give us list of columns in table
            Data[item] = tempListTostorevalues[i]
            # print(type(tempListTostorevalues[i]))
            i += 1 
        newformedDict.update(Data)
        # print(newformedDict)
        # print(tempinstanceData)
        # print(len(tempinstanceData))
        
        tempLenOfTempInstanceData = len(tempinstanceData)
        DataToInsertInNewDict = {f'{tableName}_{tempLenOfTempInstanceData}':{}}
        DataToInsertInNewDict[f'{tableName}_{tempLenOfTempInstanceData}'] = newformedDict
        tempinstanceData.update(DataToInsertInNewDict) 
        for data in schemeDataList:
            tempinstanceData[f'{tableName}_0'][f'{data}'] = None 
        writeInFile = open(f'databases/{DatabaseName}/{tableName}.py','w')
        writeInFile.write(f'{tableName}= {tempinstanceData}')
        writeInFile.close()

        ##################################################
        # requiredColumn = len(list(tempinstanceData))
        # keysOfTable = list(tempinstanceData)
        # neededSchemeofTable = list(tempinstanceData[list(tempinstanceData)[0]])
        # for data in neededSchemeofTable:
        #     if neededSchemeofTable.index(data) <requiredColumn:
        #         print('|'+neededSchemeofTable[neededSchemeofTable.index(data)]+'|  ',end='')
        #     else:
        #         continue
        # print('\n')
        # for x in keysOfTable:
        #     if keysOfTable.index(x) == 0:
        #         continue
        #     else:
        #         for i in list(tempinstanceData[x]):
        #             if list(tempinstanceData[x]).index(i) < requiredColumn:
        #                 print(tempinstanceData[x][i],'    ',end='')
        #             else:
        #                 continue
        #         print('\n')
        #################################################
    verifyData(Data)
    
# insertData(tempDB,tableName)

if __name__ == 'main':
    print('ok')