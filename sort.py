#Created by samhamnam
import os
import shutil

def start(working_dir, sorted_dir):
    #if os.path.isdir(working_dir) == True:
        #print("Found directory: "+working_dir)
    #else:
        #print("This aint no directory!")

    if os.path.isdir(sorted_dir) == False:
        os.mkdir(sorted_dir)
    
    for file in os.listdir(working_dir):
        if file.endswith(""):
            dir = os.path.abspath(file)
            #print(str(dir))
            filename, file_extension = os.path.splitext(file)
            #print(file_extension)
            if os.path.isdir(sorted_dir+"/"+file_extension) == False:
                os.mkdir(sorted_dir+"/"+file_extension)
            shutil.move(working_dir+"/"+file,sorted_dir+"/"+file_extension)

def start_ex():
    temp_work = input("Enter folder with the files:\n")
    temp_sort = input("Enter folder where the goods shall be held:\n")
    start(temp_work,temp_sort)

print(len(os.listdir("sorted")))