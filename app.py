import os
import shutil
import json 

with open('config.json', 'r') as file:
    category_map = json.load(file)

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
downloads_files = os.listdir(downloads_path)


for filename in downloads_files:
    full_path = os.path.join(downloads_path, filename)
    if os.path.isfile(full_path):
        name , ext = os.path.splitext(filename)
        ext = ext.lower()
        for cat , map_ext in category_map.items():
            if ext in map_ext:
                target_folder = os.path.join(downloads_path , cat)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                target_path = os.path.join(target_folder, filename)
                counter = 1
                while os.path.exists(target_path):
                    new_name = f"{name}_{counter}{ext}"
                    target_path = os.path.join(target_folder, new_name)
                    counter += 1
                
                try:
                        shutil.move(full_path, target_path)
                        print(f"Successfully moved: {filename} -> {target_path}")
                        print("\n--- All files have been organized! ---")
                        input("Press Enter to close this window...")
                except Exception as e:
                        print(f"COULD NOT MOVE {filename}. It might be open or in use.")
                        print(f"Error details: {e}")
