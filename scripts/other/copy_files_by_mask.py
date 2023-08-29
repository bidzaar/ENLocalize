import os
import shutil
import logging
import fnmatch

source_directory = "/home/barykin/bz/release/Localizer/src/Cognitive.Localizer/wwwroot/backend"
target_directory = "/home/barykin/bz/release/forks/ENLocalize/translations/backend"
files_to_copy = ["*.en.resx.json", "*ru.resx.json", "*Strings.resx.json", "*Resource.resx.json"]
log_file = "copy_files_by_mask.txt"

def copy_files_by_masks(source_dir, target_dir, file_masks):
    logging.basicConfig(filename=log_file, filemode='a', level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    for root, _, files in os.walk(source_dir):
        for file in files:
            for file_mask in file_masks:
                if fnmatch.fnmatch(file, file_mask):
                    source_file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(source_file_path, source_dir)
                    target_file_path = os.path.join(target_dir, relative_path)
                    target_file_dir = os.path.dirname(target_file_path)

                    if not os.path.exists(target_file_dir):
                        os.makedirs(target_file_dir)

                    try:
                        shutil.copy2(source_file_path, target_file_path)
                        logging.info(f"Copied {source_file_path} (using mask {file_mask}) -> {target_file_path}")
                    except Exception as e:
                        logging.error(f"Failed to copy {source_file_path} (using mask {file_mask}): {str(e)}")


copy_files_by_masks(source_directory, target_directory, files_to_copy)
