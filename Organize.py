#! python3

# Organize.py - this program will move a file(s) with a certain file extension to a desired folder in D:\Omar\<Extension_like_FolderName>

# e.g. >>> C:\Users\Omar\Downloads\Text File.txt >>> copy>>> D:\Omar\Document\Text Document
# each file with a certain extension needs to be on <Extension_like_FolderName> folder i.e. image.jpg >>> JPG Pictures

# run the program in CLI using >>> py Organize.py 
# TODO: Priorities what file type get checked and moved, lighters file like (Music and Images) gets moved first, then big file like mp4.
import os, shutil, logging
import Folder_name 

logging.basicConfig(level=logging.DEBUG, filename='moved_files.log', format='[%(asctime)s] %(message)s\n')

def decodeName(name):
    # NO NEED FOR THIS FUNCTION, ONLY NEEDED TO PRINT THE FILE NAMES ON SCREEN!!
    if type(name) == str: # leave unicode ones alone
        try:
            name = name.encode('utf8')
        except:
            name = name.encode('windows-1252')
    return name

# specify the type of file's extension you want to work with.
Allow_ExtensionType =  (
    '.html', '.docx', '.csv', '.pdf', '.txt', '.cfg',
    '.mp3',
    '.jpeg', '.jpg', '.png', '.avif',
    '.mp4', '.mov', '.mkv', '.wmv', '.gif'
)

# Move to... 
os.chdir('C:\\Users\\Omar') 
# specify the folders you want to scan.
Folders_to_search = ('\\Desktop', '\\Downloads', '\\Music', '\\Pictures', '\\Videos')

dst_folder = {
    # this helper dict is to sort the files with similar extension_type to a Folder! i.e all text_based files sholud be moved to Documents
    '\\Documents' : ('.html', '.docx', '.csv', '.pdf', '.txt', '.cfg'),
    '\\Music'     : ('.mp3',),
    '\\Pictures'  : ('.jpeg', '.jpg', '.png', '.avif'),
    '\\Videos'    : ('.mp4', '.mov', '.mkv', '.wmv', '.gif')
}

def create_dir(path):
    '''check and create new Folder if it doesn't exists'''
    if os.path.isdir(path): 
        return path # folder does exists!
    os.mkdir(path) # folder doesn't exists, make one.
    logging.info(f'-----NEW FOLDER CREATED----- {path}')
    return path

def FolderName(filextension):
    '''This function is to get a Folder name based on the file extension'''
    return Folder_name.Folder_file_extension.get(filextension, "Key Not Found!")

CountFiles = 0 # To count the number of files been moved

# search the folder's tree for files with certain extension type.
def main():
    global CountFiles
    for i in range(len(Folders_to_search)):
        for Folder, subFolders, FilesNames in os.walk(os.getcwd() + Folders_to_search[i]):
            # print(f'Current Folder {Folder}')

            # ignore searshing through subFolders
            del subFolders[:] # Modifying the list in place
            # This will modify ths list instead of deleting it,
            # Deleting the list will case a <NameError> upon using the list in code,
            # Deleting without using the list wont work either because that's how os.walk() work.
            #                                ¯\_(ツ)_/¯

            # Folder with 'SAFE' at the beginning of their names are ignored from being searched
            if os.path.basename(Folder).startswith('SAFE'):
                continue # ignore this Folder
            for file in FilesNames:
                FileExtension = os.path.splitext(file)[1]

                if FileExtension in Allow_ExtensionType:

                    for extension_category in dst_folder.items(): # check what kind of extension!                       
                        if FileExtension in extension_category[1]:
                            newFolderName = create_dir(f"D:\\Omar{extension_category[0]}\{FolderName(FileExtension)}")
                            
                            if os.path.exists(newFolderName + '\\' + file):
                                logging.error(f'---File: "{file}" already exists in: {newFolderName}---')  
                                break # move to the next file
                            
                            # Move the file using shutil.move() into the desired folder that matches extension type >>> D:\Omar\<Extension_like_FolderName>
                            shutil.move(fr"{Folder}\{file}", newFolderName) # Oh boy!!
                            CountFiles += 1  
                            FileSize = os.path.getsize(newFolderName + '\\' + file) / 1000 # convert to Kilobytes
                            logging.info(f'File: "{file}" Size: {FileSize}KB\n\tmoved from: {Folder} >> {newFolderName}')    
                            break # NEXT FILE PLEASE!!!
if __name__ == '__main__':
    logging.debug("Start".center(70, '-'))
    main()
    logging.debug("End".center(70, '-'))
    
    dash_separator = ''.center(20, '-')
    if CountFiles != 0:
        print(dash_separator, f"{CountFiles} Files were moved" if CountFiles >= 2 \
            else f"{CountFiles} File were moved", dash_separator, sep='\n')
    else:
        print(dash_separator, 'No Files were moved',dash_separator, sep='\n')