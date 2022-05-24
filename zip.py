import zipfile
import os

dir_path = os.getcwd()
files_path = [file_path for file_path in os.listdir(dir_path) if os.path.isfile(file_path)]
zip_path = os.path.join(dir_path, 'new.zip')
# zip_file = zipfile.ZipFile(zip_path, 'w')

with zipfile.ZipFile(zip_path, 'w') as zip_file:
    for file_path in files_path:
        zip_file.write(file_path)
