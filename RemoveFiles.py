import os
import time
import shutil

def removeFiles():
        path = "./Dummy"
        date = 0
        seconds = time.time()-(date*24*60*60)
        # seconds = 20
        numberOfDeletedFiles = 0
        numberOfDeletedFolders = 0

        if(os.path.exists(path)):
            for root_folder,folders,files in os.walk(path):
                if(seconds>= getFolderOrFileAge(root_folder)):
                    remove_folder(root_folder)
                    numberOfDeletedFolders = numberOfDeletedFolders+1
                    break 
                else:
                    for folder in folders:
                        folder_path = os.path.join(root_folder,folder)
                        if(seconds>= getFolderOrFileAge(folder_path)):
                            remove_folder(folder_path)
                            numberOfDeletedFolders = numberOfDeletedFolders+1
                        else:
                            if(seconds>= getFolderOrFileAge(path)):
                                remove_file(path)
                                numberOfDeletedFiles = numberOfDeletedFiles+1

                    for file in files :
                        file_path = os.path.join(root_folder,file)
                        if(seconds>=getFolderOrFileAge(file_path)):
                            remove_file(file_path)
                            deleted_files_count+=1
                        
        else:
            print("Path not found")

        print('Total number of deleted files '+str(numberOfDeletedFiles))
        print('Total number of deleted folders '+str(numberOfDeletedFolders))



def getFolderOrFileAge(path):
    ctime = os.stat(path).st_ctime
    return ctime

def remove_file(path):
    if(not os.remove(path)):
        print("{path} Removed Succesfully")

    else:
        print('Unable to delete files')

def remove_folder(path):
    if(not shutil.rmtree(path)):
        print('Folder Removed successfully')

    else:
        print('Unable to remove file')

removeFiles()