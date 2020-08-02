import os
import win32api
import numpy as np
selecteddir = ""
def ipfromuser():
    i = 1
    global selecteddir
    msg = "Folllowing drives are available to process:"
    drives = win32api.GetLogicalDriveStrings()
    dirName = np.array(drives.split('\000')[:-1])
    for eachd in dirName:
        msg = msg + " Enter "+ str(i) +" for " + eachd
        i += 1
    msg = msg + " ::"
    while True:
        ipt = int(input(msg))
        if ipt > 0 and (ipt <= i + 1):
            selecteddir = str(dirName[ipt - 1])
            break
        else:
            pass
    # return selecteddir        

def checkEmpty():
    global selecteddir
    listOfEmptyDirs = []
    for (dirpath, dirnames, filenames) in os.walk(selecteddir):
        if len(dirnames) == 0 and len(filenames) == 0 :
            listOfEmptyDirs.append(dirpath)
    return listOfEmptyDirs
def main():
    global selecteddir
    ipfromuser()
    listOfEmptyDirs = checkEmpty()
    if len(listOfEmptyDirs) > 0:
        print(listOfEmptyDirs)
        decision = int(input("Please enter 1 to Delete all above empty folders::"))
        if decision == 1:
            while True:
                listOfEmptyDirs = checkEmpty()
                if len(listOfEmptyDirs) > 0:
                    for dirtor in listOfEmptyDirs:
                        os.rmdir(dirtor)
                        print(dirtor,"is Removed")
                else:
                    break
        else:
            print("No files are deleted :)")
    else:
        print("Congrulations you have no Empty Dirctories in "+selecteddir+". _/\\_")
if __name__ == '__main__':
    main()