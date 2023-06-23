import os
import shutil

files = './one-k-files/files'

file_names = os.listdir(files)


languages = set()

# get language names from files
for file_name in file_names:
    language = file_name.split('-')[0]
    languages.add(language)

# creating subfolders
for language in languages:
    language_directory = os.path.join(files, language)
    if not os.path.exists(language_directory):
      os.makedirs(language_directory)

# move files to subfolders
for file_name in file_names:
    language = file_name.split('-')[0]
    source_file = os.path.join(files, file_name)
    destination_file = os.path.join(files, language, file_name)
    shutil.move(source_file, destination_file)

print('File grouping completed successfully, Please check ./one-k-files/files to see the new directories')

