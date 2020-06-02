from os import listdir,mkdir,rename
from os.path import isfile, join,splitext,exists

#folder path that were you want to take the files
INITIAL_PATH="/path/to/Watch"
#folder path that were you want to send the files
FINAL_PATH="/path/to/send"
#CONSTANT
FILE_SEPARATOR="/"

#get the filenames of the initial path
onlyfiles = [f for f in listdir(INITIAL_PATH) if isfile(join(INITIAL_PATH, f))]

#get the extension of the filename
def getExtension(filename):
    return splitext(filename)[1]

#create a folder for the given extension if not exists
def createFolder(extension):
    folderName=extension.replace(".","")
    if not exists(FINAL_PATH+FILE_SEPARATOR+folderName):
        mkdir(FINAL_PATH+FILE_SEPARATOR+folderName)
    return folderName

#move all the files
for file in onlyfiles:
    folderName = createFolder(getExtension(file))
    rename(INITIAL_PATH+FILE_SEPARATOR+file,FINAL_PATH+FILE_SEPARATOR+folderName+FILE_SEPARATOR+file)








