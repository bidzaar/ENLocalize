import os
import shutil
import logging

# Пример использования:
# source_directory = "/home/barykin/bz/release/forks/ENLocalize/translations/web/components"
# target_directory = "/home/barykin/bz/release/Localizer/src/Cognitive.Localizer/wwwroot/web/components"
# file_to_copy = "en.json"
# source_directory = "/home/barykin/bz/release/Localizer/src/Cognitive.Localizer/wwwroot/backend"
# target_directory = "/home/barykin/bz/release/emailtemplates/src"
# file_to_copy = "*.resx.json"
source_directory = "/home/barykin/bz/release/forks/ENLocalize/translations/"
target_directory = "/home/barykin/bz/release/forks/AZLocalize/translations/"
files_to_copy = "en.json"

def copy_files_by_name(source_dir, target_dir, file_name):
    log_file = "copy_files_by_name.txt"
    logging.basicConfig(filename=log_file, filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    for root, _, files in os.walk(source_dir):
        for file in files:
            if file == file_name:
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_file_path, source_dir)
                target_file_path = os.path.join(target_dir, relative_path)
                target_file_dir = os.path.dirname(target_file_path)

                if not os.path.exists(target_file_dir):
                    os.makedirs(target_file_dir)

                shutil.copy(source_file_path, target_file_path)
                logging.info(f"Copied {source_file_path} -> {target_file_path}")



copy_files_by_name(source_directory, target_directory, files_to_copy)
