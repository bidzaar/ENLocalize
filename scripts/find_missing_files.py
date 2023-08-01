import os

def list_files_in_directory(directory):
    # Функция, которая возвращает список имен файлов в заданной директории
    return set(os.listdir(directory))

def find_files_missing_in_directory(dir1, dir2):
    # Получаем списки файлов в каждой директории
    files_in_dir1 = list_files_in_directory(dir1)
    files_in_dir2 = list_files_in_directory(dir2)

    # Находим файлы, которые есть в одной из директорий, но отсутствуют в другой
    files_missing_in_dir2 = files_in_dir1 - files_in_dir2
    files_missing_in_dir1 = files_in_dir2 - files_in_dir1

    # Выводим результат
    print(f"Файлы, отсутствующие в директории {dir2}:")
    for file in files_missing_in_dir2:
        print(file)

    print(f"\nФайлы, отсутствующие в директории {dir1}:")
    for file in files_missing_in_dir1:
        print(file)

if __name__ == "__main__":
    # Укажите пути к двум директориям, которые хотите сравнить
    directory1 = "/home/barykin/bz/release/forks/ENLocalize/translations/emails/templates/ru-RU"
    directory2 = "/home/barykin/bz/release/forks/ENLocalize/translations/emails/templates/en-GB"

    find_files_missing_in_directory(directory1, directory2)
