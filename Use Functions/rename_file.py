import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"/Users/prestonc.doris/Desktop/Web Development/Udacity/Full Stack Web Dev Nano/Use Functions/secret message")
    
    current_dir = os.getcwd()
    
    os.chdir(r"/Users/prestonc.doris/Desktop/Web Development/Udacity/Full Stack Web Dev Nano/Use Functions/secret message")
    
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old file name - " + file_name)
        print("New file name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))

    os.chdir(current_dir)

rename_files()
