import os 

def selectDataBaseName():
    DatabaseName = input("[+] Enter thr Name of Database to make : ")
    if DatabaseName == '':
        while True:
            nextChoice = input('[+] Stop database making session(y/n) :')
            if nextChoice !='y' or nextChoice != 'n':
                continue
            elif nextChoice == 'y':
                False;break
            elif nextChoice == 'n':
                selectDataBaseName()
            else:
                print("[-] some error occured ")
                break
    else:
        return DatabaseName
                
class makeDataBase:
    def __init__(self,folderName):
        self.folderName = folderName
        try:
            listDirecotries = os.listdir('databases')
        except:
            os.mkdir('databases')  
        try: 
            os.mkdir(f'databases/{self.folderName}')
        except:
            return "already made"

def madeDB():
    tempDb = selectDataBaseName()
    makeDataBase(tempDb)
    print(f'[+]{tempDb} is formed')
if __name__ == '__main__':
    print()
# madeDB()