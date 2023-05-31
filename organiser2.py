import os
import shutil

from_dir = "/Users/lilydalmia/Downloads"
to_dir = "/Users/lilydalmia/Downloads"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file in list_of_files:
    name,extension = os.path.splitext(file)
    print(name)
    print(extension)

    if(extension == ""):
        continue
    if(extension in [".pdf",".doc",".docx",".txt"]):
        path1 = from_dir + "/" + file
        path2 = to_dir + "/" + "docs"
        path3 = to_dir + "/" + "docs" + "/" + file
        
        print(path1)
        print(path2)
        print(path3)

        if(os.path.exists(path2)):
            print("moving " + file)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving " + file)
            shutil.move(path1,path3)
