import os

directory = '/home/barykin/bz/release/forks/ENLocalize/translations/backend'
source = 'en-gb'
destination = 'en'

def rename_files_recursive(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if source.lower() in filename.lower():
                new_filename = filename.replace(source, destination, 1)
                original_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)
                os.rename(original_path, new_path)
                print(f'Renamed: {original_path} -> {new_path}')

rename_files_recursive(directory)