import importlib
from os import path , removedirs , remove


def deleteDB(DataBaseName):
    decision = input("[+]DO you really want to delete current database (y/n) :")
    if decision == 'y':
        reality = path.isdir(f'databases/{DataBaseName}')
        if reality == True:
            removedirs(f'database/{DataBaseName}')

def deletetable(DataBaseName,TableName):
    if path.isfile(f'databases/{DataBaseName}/{TableName}') == True:
        remove(f'databases/{DataBaseName}/{TableName}.py')
        remove(f'databases/{DataBaseName}/cache_{TableName}.py')

def deleteEntry(DataBaseName,TableName,conditionColumn,condition):
    selectedData = importlib.import_module(f'databases.{DataBaseName}.{TableName}')
    Data = selectedData.__dict__.get(f'{TableName}') # complete data
    # print(list(Data)) # list of users 
    for x in list(Data):
        for i in list(Data[x]):
            if i == conditionColumn or conditionColumn == '*':
                if Data[x][i] == condition:
                    Data.pop(x)
                    f = open(f'databases/{DataBaseName}/{TableName}.py','w')
                    f.write(f'{TableName} = {Data}')
                    f.close()


# deleteEntry('newDB','users','uname','random')