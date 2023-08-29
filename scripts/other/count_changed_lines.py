import subprocess

def count_changed_lines(branch):
    # Получаем вывод команды git diff для подсчета измененных строк
    diff_output = subprocess.check_output(["git", "diff", "-U0", "HEAD..{}".format(branch)]).decode("utf-8")
    
    # Разделяем вывод на строки и подсчитываем измененные строки
    lines = diff_output.strip().split('\n')
    changed_lines = 0
    
    for line in lines:
        if line.startswith('+') or line.startswith('-'):
            changed_lines += 1
    
    return changed_lines

if __name__ == "__main__":
    branch_name = "releasetr-3.18"  # Замените на имя вашей ветки
    changed = count_changed_lines(branch_name)
    print("Изменено строк:", changed)