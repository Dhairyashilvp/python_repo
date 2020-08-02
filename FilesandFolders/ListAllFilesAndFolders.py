import os
import win32api
import numpy as np
import json
extlist = (".aiff",".au",".avi",".bat",".bmp",".bin",".class",".csv",".cvs",".dbf",".dif",".doc",".eps",".exe",".fm3",".gif",".hqx",".htm",".html",".jpg",".mac",".map",".mdb",".mid",".mov",".mtb",".msi",".pdf",".p65",".t65",".png",".ppt",".psd",".psp",".qxd",".ra",".rtf",".sit",".tar",".tif",".txt",".wav",".wk3",".wks","wpd",".xls",".xml",".zip")
excludedir = ["SpringB", "System Volume Information", "VM's", "VMWare", "configuration", "cache", "user_data", "htdocks", "log", "LOST.DIR", "Android", "Backup", "Install", "Photos", "WhatsApp", ".thumbnails", ".Thumbs", ".trash", ".Shared", "Databases", ".Statuses", "", ""]
finaldict = {}
drives = win32api.GetLogicalDriveStrings()
drives = np.array(drives.split('\000')[:-1])
#loop through every folder
def extractdata(dirPath,prevdir=""):
    files = []
    documentFile ={}
    if prevdir == "":
        prevdir = dirPath
    filesAndFolderslList = os.listdir(dirPath)
    for filesAndFolders in filesAndFolderslList:
        if filesAndFolders.lower().endswith(extlist) or os.path.isfile(dirPath+"\\"+filesAndFolders):
            files.append(filesAndFolders)
            if  documentFile.get(prevdir):
                documentFile['files'] = files
            else:
                documentFile['files'] = files
        else:
            if filesAndFolders not in excludedir and len(os.listdir(dirPath+"\\"+filesAndFolders)) > 0 :
                if  documentFile.get(prevdir):   
                    documentFile[filesAndFolders] = extractdata(dirPath+"\\"+filesAndFolders,filesAndFolders)
                else:
                    documentFile[filesAndFolders] = extractdata(dirPath+"\\"+filesAndFolders,filesAndFolders)
    return documentFile
for driveName in drives[2:4]:
    fileName = driveName.replace(":\\","")+"_drive"
    finaldict = extractdata(driveName,"")
    f = open(fileName+".json", "w")
    f.write(json.dumps(finaldict))
    f.close()