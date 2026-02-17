# Whrite the automation script to which copy all file from source directry to Destinatiion Directry 

import sys
import os
import shutil

def DirectoryFileSearch(DirName,DestDir):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directry")
        return

    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("There is no not directry")
        return
    
    os.makedirs(DestDir,exist_ok=True)
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):        # To walk/Scan directry 
        for File in FileName:
            SourceFilePath = os.path.join(FolderName, File)
            DestFilePath = os.path.join(DestDir, File)

            try:
                shutil.copy(SourceFilePath,DestFilePath)
            except Exception as e:
                print(e)
            
    

def main():
    Border = "_"*60
    print(Border)
    print("-----------------Vivek Directory Automation-----------------")
    print(Border)

    if(len(sys.argv) != 3):
        print("Invalid number of argument")
        print("Please specify the name of directory and Destination folder name ")
        return
    
    DirectoryFileSearch(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()