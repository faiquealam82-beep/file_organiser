import os
import shutil

folder_path = r"C:\Users\Faique\Downloads"
print(folder_path)

items = os.listdir(folder_path)
print(items)

images_folder = os.path.join(folder_path, "Images")
os.makedirs(images_folder, exist_ok=True)

pdfs_folder = os.path.join(folder_path, "PDFs")
os.makedirs(pdfs_folder, exist_ok=True)

videos_folder = os.path.join(folder_path, "Videos")
os.makedirs(videos_folder, exist_ok=True)

zip_folder = os.path.join(folder_path, "ZIP files")
os.makedirs(zip_folder, exist_ok=True)

installers_folder = os.path.join(folder_path, "INSTALLERS")
os.makedirs(installers_folder, exist_ok=True)

for item in items:
    print(item)

    full_path = os.path.join(folder_path, item) 
    print(full_path)

    
    name, extension = os.path.splitext(item)
    print("File Name :", name)
    print("Extension :", extension)

    extension = extension.lower()

    if extension in [".jpg", ".jpeg", ".png"]:
       print(item, "is an IMAGE")
       shutil.move(full_path, images_folder)
       print(item, "has been moved.")

    if extension in [".pdf"]:
       print(item, "is a PDF")
       shutil.move(full_path, pdfs_folder)
       print(item, "has been moved.") 

    if extension in [".mp4", ".mkv", ".avi"]:
       print(item, "is a Video")
       shutil.move(full_path, videos_folder)
       print(item, "has been moved.")

    if extension in [".zip"]:
       print(item, "is a ZIP ifle")
       shutil.move(full_path, zip_folder) 
       print(item, "has been moved") 

       
    if extension in [".exe", ".msi"]:
       print(item, "is an INSTALLER")
       shutil.move(full_path, installers_folder)
       print(item, "has been moved")



    if os.path.isfile(full_path):
      print(item, "is a FILE")
    
    else:
        print(item, "is a FOLDER")







