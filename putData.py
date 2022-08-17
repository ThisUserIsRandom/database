from importlib import import_module
from operator import index

tableName = 'storedate'
tempTableName = 'cache_'+tableName
tempDB = 'newDbb'

def importTableCache(DatabaseName,tableName):
    cacheFile = import_module(f"databases.{DatabaseName}.{tableName}")
    return  cacheFile

def importTable(DatabaseName,tableName):
    mainFile = import_module(f'databases.{DatabaseName}.{tableName}')
    return mainFile

def insertData(DatabaseName,tableName):#,DataToInsert
    schemeofTable = import_module(f"databases.{DatabaseName}.{tempTableName}")  
    contentofTable = importTable(tempDB,tempTableName)
    tableData = import_module(f"databases.{DatabaseName}.{tableName}")
    tempinstanceData = tableData.__dict__.get(f'{tableName}') 
    tableTamplate = list(tempinstanceData)[0]
    Data = tempinstanceData[tableTamplate] 
    def verifyData(Data):
        newformedDict = {}
        ListData = list(Data)
        tempListTostorevalues = []
        for item in ListData:
            enterData = input(f'enter {item} :')
            tempListTostorevalues.append(enterData)
        i = 0
        for item in ListData:
            Data[item] = tempListTostorevalues[i]
            i += 1
        newformedDict.update(Data)
        tempLenOfTempInstanceData = len(tempinstanceData)
        DataToInsertInNewDict = {f'{tableName}_{tempLenOfTempInstanceData}':{}}
        DataToInsertInNewDict[f'{tableName}_{tempLenOfTempInstanceData}'] = Data
        # print(DataToInsertInNewDict)
        tempinstanceData.update(DataToInsertInNewDict)
        dictofTable = tableData.__dict__.get(f'{tableName}')
        writeInFile = open(f'databases/{tempDB}/{tableName}.py','w')
        writeInFile.write(f'{tableName}= {tempinstanceData}')
        writeInFile.close()

        ##################################################
        requiredColumn = 1
        keysOfTable = list(tempinstanceData)
        neededSchemeofTable = list(tempinstanceData[list(tempinstanceData)[0]])
        for data in neededSchemeofTable:
            if neededSchemeofTable.index(data) <requiredColumn:
                print('|'+neededSchemeofTable[neededSchemeofTable.index(data)]+'|  ',end='')
            else:
                continue
        print('\n')
        for x in keysOfTable:
            if keysOfTable.index(x) == 0:
                continue
            else:
                for i in list(tempinstanceData[x]):
                    if list(tempinstanceData[x]).index(i) < requiredColumn:
                        print(tempinstanceData[x][i]+'    ',end='')
                    else:
                        continue
                print('\n')
        #################################################
    verifyData(Data)
    
insertData(tempDB,tableName)

