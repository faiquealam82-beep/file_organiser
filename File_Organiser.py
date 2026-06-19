import os
import shutil
import json
import pyttsx3
engine = pyttsx3.init()


with open("mapping_rules.json", "r") as file:
   mapping_rules = json.load(file)

print(mapping_rules)   

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

   for ext, folder_name in mapping_rules.items():
         folder_path_created = os.path.join(folder_path, folder_name)
         os.makedirs(folder_path_created, exist_ok=True)

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

         if destination_folder is None:

            print("Unknown extension detected Sir:", extension)

            engine.say(f"Unknown extension detected, Sir. {extension}")
            engine.runAndWait()

            folder_name = input("Enter folder name for this extension: ")

            destination_folder = os.path.join(folder_path, folder_name)
            os.makedirs(destination_folder, exist_ok=True)

            mapping_rules[extension] = folder_name
            
            with open("mapping_rules.json", "w") as file:
               json.dump(mapping_rules, file, indent=4)
               
            extension_map[extension] = destination_folder

         if destination_folder:

            destination_path = os.path.join(destination_folder, item)
            if not os.path.exists(destination_path):

               shutil.move(full_path, destination_folder)
               print(item, "has been moved.")

            else:
               print(item, "already exists. Skipping...")   

organize_folder(r"C:\Users\Faique\Downloads")
   
   








