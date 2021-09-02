#! python3

# Organize.py - this program will move a file(s) with a certain file extension to a desired folder in D:\Omar\<Extension_like_FolderName>

# e.g. >>> C:\Users\Omar\Downloads\Text File.txt >>> copy>>> D:\Omar\Document\Text Document
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
Allow_ExtensionType =  (
    '.html', '.docx', '.csv', '.pdf', '.txt',
    '.mp3',
    '.mp4', '.mov', '.mkv', '.wmv',
    '.jpeg', '.jpg', '.png', '.avif', '.gif'
)

# Move to... 
os.chdir('C:\\Users\\Omar') 
# specify the folders you want to scan.
Folders_to_search = ('\\Desktop', '\\Downloads', '\\Music', '\\Pictures', '\\Videos')

dst_folder = {
    # this helper dict is to sort the files with similar extension_type to a Folder! i.e all text_based files sholud be moved to Documents
    '\\Documents' : ('.html', '.docx', '.csv', '.pdf', '.txt'),
    '\\Music'     : ('.mp3',),
    '\\Pictures'  : ('.jpeg', '.jpg', '.png', '.avif'),
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
        '.html': 'HTML',   # HTML Document

        # inside the Music Floder
        '.mp3': 'MP3',     # MP3 Music
        
        # inside the pictures Folder
        '.jpeg': 'JPEG',   # JPEG Pictures
        '.jpg': 'JPG',     # JPG Pictures   
        '.png': 'PNG',     # PNG Pictures
        '.avif': 'AVIF',   # AVIF Pictures
        
        # inside the Videos Folder
        '.mp4': 'MP4',     # MP4 Videos
        '.mov': 'MOV',     # MOV Videos
        '.mkv': 'MKV',     # MKV Videos
        '.wmv': 'WMV',     # WMV Videos
        '.gif': 'GIF'      # GIF Videos
    }
    return format_file_extension.get(filexe, "Key Not Found!")

# search the folder's tree for files with certain extension type.
def main():
    for i in range(len(Folders_to_search)):
        for Folder, subFolder, FilesNames in os.walk(os.getcwd() + Folders_to_search[i]):
            # print(f'Current Folder {Folder}')
                    
            for file in FilesNames:
                FileExtension = os.path.splitext(file)[1]

                if FileExtension in Allow_ExtensionType:

                    for extension_catagory in dst_folder.items(): # check what kind of extension!                       
                        if FileExtension in extension_catagory[1]:
                            newFolderName = create_dir(f"D:\\Omar{extension_catagory[0]}\{FolderName(FileExtension)} {extension_catagory[0][1:]}")
                            
                            if os.path.exists(newFolderName + '\\' + file):
                                logging.debug(f'File already exists in: {newFolderName}')  
                                break # move to the next file
                            
                            # Move the file using shutil.move() into the desired folder that matches extesion type >>> D:\Omar\<Extension_like_FolderName>
                            shutil.move(fr"{Folder}\{file}", newFolderName) # Oh boy!!
                            logging.info(f'File moved to: {newFolderName}')    
                            break # NEXT FILE PLEASE!!!

# TODO: move the folder that holds the content insted of moving the content them self, for better organization!
    # the Problem with this is if there is a *.txt inside a Pictures folder with xNum photos!
        # what's gonna happend to this .txt?
            # MAYBE! create a parent folder with the same name of that folder to only
            # contain the .txt file and then move this folder inside Text Document!
            # not really cool but yeah you gonna end up with a lot of folder <LOL/>
            
if __name__ == '__main__':
    main()