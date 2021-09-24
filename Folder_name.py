r'''
This file is for adding, removing and modifying Folder Names that correspond to a file extension
You can't use these characters \\/:*?"<>| for naming folders in Windows OS, this will produce a 
 FileNotFoundError: [WinError 3] The system cannot find the path specified: <file_path>
'''

Folder_file_extension = {

    # inside the Document Floder   
    '.docx': 'Word Documents',   # Word Documents
    '.csv': 'Excel Documents',   # Execl Documents
    '.pdf': 'PDF Documents',     # PDF Documents
    '.txt': 'Text Documents',    # Text Documents
    '.html': 'HTML Documents',   # HTML Documents
    '.cfg': 'Configuration Files',  # Configuration Files

    # inside the Music Floder
    '.mp3': 'MP3 Music',     # MP3 Music
    
    # inside the pictures Folder
    '.jpeg': 'JPEG Pictures',   # JPEG Pictures
    '.jpg': 'JPG Pictures',     # JPG Pictures   
    '.png': 'PNG Pictures',     # PNG Pictures
    '.avif': 'AVIF Pictures',   # AVIF Pictures
    
    # inside the Videos Folder
    '.mp4': 'MP4 Videos',     # MP4 Videos
    '.mov': 'MOV Videos',     # MOV Videos
    '.mkv': 'MKV Videos',     # MKV Videos
    '.wmv': 'WMV Videos',     # WMV Videos
    '.gif': 'GIF Videos'      # GIF Videos
}