#! python3

# Organize.py - this program will copy a file(s) with a certain file extension to a desired folder in D:\Omar\<Extension_like_FolderName>

# e.g. >>> C:\Users\Omar\Downloads\Text File.txt >>> copy>>> D:\Omar\Text Document
# each file with a certain extension needs to be on <Extension_like_FolderName> folder i.e. image.jpg >>> JPG Pictures

# run the program in CLI using >>> py Organize.py 

import os, shutil, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

def decodeName(name):
    # NO NEED FOR THIS FUNCTION, ONLY NEEDED TO PRINT ON SCREEN!!
    if type(name) == str: # leave unicode ones alone
        try:
            name = name.encode('utf8')
        except:
            name = name.encode('windows-1252')
    return name

# specify the type of file's extension you want to work with.
Allow_ExtensionType =  ('.docx', '.csv', '.pdf', '.txt', '.mp3', '.mp4', '.mov', '.mkv', '.wmv', '.jpg', '.png', '.avif', '.gif')
# specify the folders you want to scan.
Folders_to_scan = ('\\Desktop', '\\Documents', '\\Downloads', '\\Music', '\\Pictures', '\\Videos')

dst_folder = {
    # this helper dict is to sort the files with similar extension_type to a Folder! i.e all text_based files sholud be moved to Documents
    '\\Documents' : ('.docx', '.csv', '.pdf', '.txt'),
    '\\Music'     : ('.mp3',),
    '\\Pictures'  : ('.jpg', '.png', '.avif'),
    '\\Videos'    : ('.mp4', '.mov', '.mkv', '.wmv', '.gif')
}

def create_dir(path):
    '''check and create new Folder if it doesn't exists'''
    if os.path.isdir(path): 
        return path # folder does exists!
    os.mkdir(path) # folder doesn't exists, make one.
    return path

def FolderName(filexe):
    '''This function is to customize the Folder name based on the file extension'''
    format_file_extension = {
        # inside the Document Floder
        '.docx': 'Word',   # Word Document
        '.csv': 'Excel',   # Execl Document
        '.pdf': 'PDF',     # PDF Document
        '.txt': 'Text',    # Text Document

        # inside the Music Floder
        '.mp3': 'MP3',     # MP3 Music
        
        # inside the pictures Folder
        '.jpg': 'JPG',     # JPG Pictures   
        '.png': 'PNG',     # PNG Pictures
        '.avif': 'AVIF',   # AVIF Pictures
        
        # inside the Videos Folder
        '.mp4': 'MP4',     # MP4 Videos
        '.mov': 'MOV',     # MOV Videos
        '.mkv': 'MKV',     # MKV Videos
        '.wmv': 'WMV',     # WMV Videos
        '.gif': 'GIF'       # GIF Videos
    }
    return format_file_extension.get(filexe, "Key Not Found!")


# move to and search the folder's tree for files with certain extension type.
os.chdir('C:\\Users\\Omar')
for i in range(len(Folders_to_scan)):
    for Folder, subFolder, FilesNames in os.walk(os.getcwd() + Folders_to_scan[i]):
        # print(f'Current Folder {Folder}')
                
        for file in FilesNames:
            FileExtension = os.path.splitext(file)[1]

            if FileExtension in Allow_ExtensionType:

                    for extension_catagory in dst_folder.items(): # check what kind of extension!                       
                        if FileExtension in extension_catagory[1]:
                            newFolderName = create_dir(f"D:\\Omar{extension_catagory[0]}\{FolderName(FileExtension)} {extension_catagory[0][1:]}")
                            
                            if os.path.exists(newFolderName + '\\' + file):
                                logging.info(f'File already exists in folder: {newFolderName}')  
                                break # move to the next file
                            
                            # Copy the file using shutil.copy into the desired folder that matches extesion type >>> D:\Omar\<Extension_like_FolderName>
                            shutil.copy(fr"{Folder}\{file}", newFolderName)
                            logging.debug(f'File copied to >>> {newFolderName}')    
                            break # NEXT FILE PLEASE!!!