import os
import shutil
from pathlib import Path

def remove_segMENt():
    os.chdir(r"C:\Users\mohit\Downloads\img_highres_seg-011\img_highres\MEN")
    print(os.getcwd())
    path="C:/Users/mohit/Downloads/img_highres_seg-011/img_highres/MEN"
    main_files=os.listdir(r"C:\Users\mohit\Downloads\img_highres_seg-011\img_highres\MEN")

    for mf in main_files:
        next_path=path+"/"+str(mf)
        next_path_file=os.listdir(next_path)
        for npf in next_path_file:
            final_path=next_path+"/"+str(npf)
            pather=final_path+'/'
            for file_name in os.listdir(pather):
                seg='segMENt'
                if seg in file_name:
                    path_img=os.path.join(pather,file_name)
                    os.remove(path_img)

def rename_file():
    os.chdir(r"C:\Users\mohit\Downloads\img_highres_seg-011\img_highres\MEN")

    print(os.getcwd())
    path="C:/Users/mohit/Downloads/img_highres_seg-011/img_highres/MEN"
    main_files=os.listdir(r"C:\Users\mohit\Downloads\img_highres_seg-011\img_highres\MEN")

    for mf in main_files:
        counter=0
        next_path=path+"/"+str(mf)
        next_path_file=os.listdir(next_path)
        for npf in next_path_file:
            final_path=next_path+"/"+str(npf)
            pather=final_path+'/'
            for file_name in os.listdir(pather):
                oldfile_pather=pather+"/"+file_name
                newfile_name=mf+str(counter)+".jpg"
                next_path_filer=pather+newfile_name
                os.rename(oldfile_pather,next_path_filer)
                counter+=1

def move_file():
    os.chdir(r"C:\Users\mohit\Downloads\img_highres_seg-011\img_highres\MEN")

    print(os.getcwd())
    path="C:/Users/mohit/Downloads/img_highres_seg-011/img_highres/MEN"
    main_files=os.listdir(r"C:\Users\mohit\Downloads\img_highres_seg-011\img_highres\MEN")

    #listing the categories such as tees, pants
    for mf in main_files:
        next_path=path+"/"+str(mf)
        next_path_file=os.listdir(next_path)
        
        #list the id numbers
        for npf in next_path_file:
            final_path=next_path+"/"+str(npf)
            pather=final_path+'/'

            #lists the final images
            for file_name in os.listdir(pather):
                new_file_path=next_path+"/"+file_name
                old_file_path=pather+file_name
                shutil.move(old_file_path,new_file_path)

if __name__=='__main__':
    #execute finctions in above sequence
    print("Hello")

