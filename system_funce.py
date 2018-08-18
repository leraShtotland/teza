import os
#move files from one folder to another folder

def move_files():
    folder_poster = "C:\\Users\\lera\\Desktop\\1108\\posters_0708\\"
    folder_move = "C:\\Users\\lera\\Desktop\\1108\\poster_move\\"
    counter = 43610
    for i in range(43610, 45070):
        path=folder_poster + str(i) + ".jpg"
        path_move=folder_move+ str(i) + ".jpg"
        #os.path.join()
        os.rename(path, path_move)


#move_files()


import os
from os import listdir
from os.path import isfile, join

def read_from_txt(path):
    with open(path) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

def delete_image_from_file(content_list):
    for file in content_list:
        os.remove(file)

#get the names of all files in folder
def get_files_in_folder(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles


# path="grey_images.txt"
# content=read_from_txt(path)
# delete_image_from_file(content)
path="C:\\Users\\lerasht\\Desktop\\posters_0908"
get_files_in_folder(path)

#return list with all the absolute paths in the directory
#then we can open each image in the list
def absoluteFilePaths(path):
    list_abs_paths=[]
    for path, subdirs, files in os.walk(path):
        for name in files:
            list_abs_paths.append(os.path.join(path, name))
    return list_abs_paths

