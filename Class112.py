import os
import shutil


from_dir="C:/Users/17034/Downloads/Images"
to_dir="C:/Users/17034/Downloads/Move"

list_of_files=os.listdir(from_dir)
# print(list_of_files)

for i in list_of_files:
    # print(i)
    name,extension=os.path.splitext(i)
    print(name)
    
    if extension in ['.gif','.jpg','.png','.jpeg']:

        path1=from_dir+"/"+i
        path2=to_dir+"/"+"Image_files"
        path3=to_dir+"/"+"Image_files"+"/"+i

        if os.path.exists(path2):
            print("moving "+i+"......")
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print("Moving  "+i+".......")
            shutil.move(path1,path3)    