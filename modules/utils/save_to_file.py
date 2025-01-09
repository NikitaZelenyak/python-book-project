import json

def save_to_file(file_path, data):
   print(data)
   with open(file_path, "w") as file:
        json.dump(data, file, indent=4)