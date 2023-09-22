import os
import json
import logging
import glob

# Переменные для настройки скрипта
#for backend
base_directory = "/home/barykin/bz/release/forks/AZLocalize/translations/web/"
target_directory = "/home/barykin/bz/release/Localizer/src/Cognitive.Localizer/wwwroot/web/"
# base_directory = "/home/barykin/bz/release/forks/ENLocalize/translations/emails/forks/AZN_FORK/subjects/en-GB"
# target_directory = "/home/barykin/bz/release/emailtemplates/src/forks/AZN_FORK/subjects/en-GB"


log_file_path = "compare_and_update_jsons_by_mask.txt"
json_file_pattern = "az.json"  # Маска для имен файлов

def update_json(target_data, base_data):
    modified = False
    if isinstance(target_data, dict) and isinstance(base_data, dict):
        for key, value in base_data.items():
            if key not in target_data:
                target_data[key] = value
                modified = True
            elif isinstance(value, dict):
                modified |= update_json(target_data[key], value)
            else:
                if target_data[key] != value:
                    target_data[key] = value
                    modified = True
    return modified

def compare_and_update_json(base_path, target_path):
    if os.path.exists(target_path):
        with open(base_path, 'r', encoding='utf-8') as base_file, open(target_path, 'r+', encoding='utf-8') as target_file:
            try:
                base_data = json.load(base_file)
                target_data = json.load(target_file)

                modified = update_json(target_data, base_data)

                if modified:
                    target_file.seek(0)
                    target_file.truncate(0)
                    json.dump(target_data, target_file, indent=4, ensure_ascii=False)
                    logging.info(f"Updated: {target_path}")

            except json.JSONDecodeError:
                logging.error(f"Error decoding JSON in file: {target_path}")

    else:
        logging.warning(f"File not found in target directory: {target_path}")
        logging.info(f"Base file path: {base_path}")

def compare_and_update_jsons(base_dir, target_dir):
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(message)s')

    for root, _, files in os.walk(base_dir):
        for filename in glob.glob(os.path.join(root, json_file_pattern)):
            base_path = filename
            target_path = os.path.join(target_dir, os.path.relpath(base_path, base_dir))
            compare_and_update_json(base_path, target_path)

if __name__ == "__main__":
    compare_and_update_jsons(base_directory, target_directory)