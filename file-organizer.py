import os
import shutil

def organize_files(folder_path): #defines function organize-files
    for filename in os.listdir(folder_path): #listsout all files and folders
        file_path = os.path.join(folder_path, filename) #creates file path
        if os.path.isfile(file_path): #only if it is file not folder
            ext = filename.split('.')[-1].lower() # gets file extention
            if ext in ['jpg', 'png', 'jpeg']: #checks the extension type
                target_folder = os.path.join(folder_path, 'Images') # assigns the files based on extension type
            elif ext in ['pdf', 'docx', 'txt']:
                target_folder = os.path.join(folder_path, 'Docs')
            elif ext in ['mp4', 'mkv']:
                target_folder = os.path.join(folder_path, 'Videos')
            else:
                target_folder = os.path.join(folder_path, 'Others')
            
            os.makedirs(target_folder, exist_ok=True) #creats folder when folder does not exists
            shutil.move(file_path, os.path.join(target_folder, filename)) # moves the files to the choosen folder

organize_files("C:/Users/nagas/Downloads") #calling function