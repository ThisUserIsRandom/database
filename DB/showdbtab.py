from os import path , listdir
from types import NoneType

def askInput(WhattoSearch,DatabaseName):
    try:
        if WhattoSearch == 'DB':
            content = listdir(f'databases')
            print("[+]Databases >")
            for chaps in content:
                if type(chaps) != NoneType:
                    #print(checkFolderorFile(chaps).split('.'))
                    if len(chaps.split('.')) < 2: # this implies this is a file
                        print(f" / {chaps}") 
        elif WhattoSearch == 'files':
            content = listdir(f'databases/{DatabaseName}')
            if len(content) == 0:
                print("[+] this Database have no files")
            print(f"[+]Tables in {DatabaseName} >")
            for chaps in content:
                if type(chaps) != NoneType:
                    #print(checkFolderorFile(chaps).split('.'))
                    if len(chaps.split('.')) >= 2: # this implies this is a file
                        if chaps.split('.',1)[1] == 'py':
                            if chaps.split('.',1)[0].split('_',1)[0] != 'cache':
                                print(f" / {chaps.split('.',1)[0]}") 
    except Exception as e:
        print(e)
# askInput('DB','newDb')