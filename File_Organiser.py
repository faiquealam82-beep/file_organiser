import os
import shutil

def organize_folder(folder_path):
   print(folder_path)

   items = os.listdir(folder_path)
   print(items)

   categories = {

      "Images": [".jpg", ".png", ".jpeg"],
      
      "PDFs": [".pdf"],

      "Videos": [".mp4", ".mkv", ".avi"],

      "ZIP files": [".zip"],

      "INSTALLERS": [".exe", ".msi"],

   }

   extension_map = {}

   for folder_name, extensions in categories.items():

      folder_path_created = os.path.join(folder_path, folder_name)
      os.makedirs(folder_path_created, exist_ok=True)

      for ext in extensions:
         extension_map[ext] = folder_path_created

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


   
   








