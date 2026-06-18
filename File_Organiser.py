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

extension_map = {

    ".jpg": images_folder,
    ".jpeg": images_folder,
    ".png": images_folder,

    ".pdf": pdfs_folder,

    ".mp4": videos_folder,
    ".mkv": videos_folder,
    ".avi": videos_folder,

    ".zip": zip_folder,

    ".exe": installers_folder,
    ".msi": installers_folder,
}

for item in items:
    print(item)

    full_path = os.path.join(folder_path, item)

    if os.path.isfile(full_path):
      print(full_path)

      name, extension = os.path.splitext(item)
      print("File Name :", name)
      print("Extension :", extension)

      extension = extension.lower()

      destination_folder = extension_map.get(extension)
      print("Destination Folder:", destination_folder)

      if destination_folder:

         destination_path = os.path.join(destination_folder, item)
         if not os.path.exists(destination_path):

            shutil.move(full_path, destination_folder)
            print(item, "has been moved.")

         else:
            print(item, "already exists. Skipping...")   


   
   








