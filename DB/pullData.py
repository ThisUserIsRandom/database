import importlib

def makeLiteralTable(DatabaseName,TableName,columns):
    TableInfo = importlib.import_module(f'databases.{DatabaseName}.{TableName}')
    cache_TableInfo = importlib.import_module(f'databases.{DatabaseName}.cache_{TableName}')
    precious = TableInfo.__dict__.get(f'{TableName}')
    myprecious = cache_TableInfo.__dict__.get(f'{TableName}')
    # print(precious)
    # print(myprecious)
    def calcSpace(dictOfdicts):
        MainList = []
        listOfDict = list(dictOfdicts)
        for column in list(myprecious):
            tempList = []
            for key in listOfDict:
                    if dictOfdicts[key][column] != None:
                                tempList.append(len(str(dictOfdicts[key][column])))
                                tempList.append(len(column))
            
            if tempList != []:
                MainList.append(max(tempList))
            tempList = []
        # print(MainList)
        for column in list(myprecious):
            if column in columns or columns==['*']:
            # print(MainList[list(myprecious).index(column)]-len(str(column)))
                print('| ',column,' '*(MainList[list(myprecious).index(column)]-len(str(column))),' |',end='')
            # print(f'{column} max len is {MainList[list(myprecious).index(column)]}')
        #print('_'*sum(MainList))
        for key in list(dictOfdicts):
            for column in list(myprecious):
                if column in columns or columns==['*']:
                    if (dictOfdicts[key][column]) != None:
                        print('| ',dictOfdicts[key][column],' '*(MainList[list(myprecious).index(column)]-len(str(dictOfdicts[key][column]))),' |',end='')
            print('\n')
    calcSpace(precious)
# makeLiteralTable('newDb','userdata') 
    