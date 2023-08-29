import sys
import subprocess

def get_commit_changes(commit_hash):
    try:
        # Получаем результат выполнения команды git diff-tree для указанного коммита
        diff_output = subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-status', '-r', commit_hash])

        # Разделяем результат на строки
        diff_lines = diff_output.decode('utf-8').splitlines()

        # Создаем списки для измененных, добавленных и удаленных файлов
        modified_files = []
        added_files = []
        deleted_files = []

        # Обрабатываем каждую строку результата
        for line in diff_lines:
            status, filename = line.split('\t', 1)
            if status == 'M':
                modified_files.append(filename)
            elif status == 'A':
                added_files.append(filename)
            elif status == 'D':
                deleted_files.append(filename)

        # Записываем списки измененных, добавленных и удаленных файлов в файл
        with open('commit_changes.txt', 'w') as f:
            f.write('Измененные файлы:\n')
            for file in modified_files:
                f.write(file + '\n')

            f.write('\nДобавленные файлы:\n')
            for file in added_files:
                f.write(file + '\n')

            f.write('\nУдаленные файлы:\n')
            for file in deleted_files:
                f.write(file + '\n')

        print('Изменения для коммита', commit_hash, 'были сохранены в файл commit_changes.txt')

    except subprocess.CalledProcessError as e:
        print('Ошибка при выполнении команды Git:', e)

# Получаем ввод коммита из аргументов командной строки
if len(sys.argv) > 1:
    commit_hash = sys.argv[1]
    get_commit_changes(commit_hash)
else:
    print('Необходимо указать хэш коммита в качестве аргумента командной строки.')
