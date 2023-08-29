import subprocess

def count_changed_lines(commit_hash):
    # Получаем вывод команды git diff для подсчета измененных строк в конкретном коммите
    diff_output = subprocess.check_output(["git", "diff", "-U0", commit_hash + "~.."+commit_hash]).decode("utf-8")
    
    # Разделяем вывод на строки и подсчитываем измененные строки
    lines = diff_output.strip().split('\n')
    changed_lines = 0
    
    for line in lines:
        if line.startswith('+') or line.startswith('-'):
            changed_lines += 1
    
    return changed_lines

if __name__ == "__main__":
    #4.1.1 
    start_commit = "8656bef7b39f76e50d1ae20add29a7e916c2a0bf" #4.1.1 "ffc28eb64d290b38b3b7d36f103ab5f03a28f1a6"  # Замените на начальный коммит
    end_commit = "a27a132cfc1b17a9d35e4b7c75e00dd1c22dad18" #4.1.1 "002b3b3b72190a45677b6e8eede19d22234c9dc1"    # Замените на конечный коммит

    user_filter = input("Введите имя или email пользователя для фильтрации (пустая строка - без фильтрации): ")
    
    commit_info = subprocess.check_output(["git", "log", "--format=%H;%an;%ae;%ad", "{}..{}".format(start_commit, end_commit)]).decode("utf-8").split('\n')
    commit_info = [info for info in commit_info if info]  # Убираем пустые строки
    
    total_changed_lines = 0
    user_stats = {}  # Словарь для хранения статистики по пользователям
    
    for info in commit_info:
        commit_hash, author_name, author_email, commit_date = info.split(';')
        
        # Фильтрация по пользователю
        if not user_filter or user_filter in author_name or user_filter in author_email:
            changed = count_changed_lines(commit_hash)
            total_changed_lines += changed

            if author_email in user_stats:
                user_stats[author_email]["lines_changed"] += changed
                user_stats[author_email]["commits"] += 1
            else:
                user_stats[author_email] = {"lines_changed": changed, "commits": 1}

            print("Коммит:", commit_hash)
            print("Автор:", author_name)
            print("Дата:", commit_date)
            print("Изменено строк:", changed)
            print("=" * 40)
    
    print("Итого изменено строк:", total_changed_lines)
    print("\nСтатистика по пользователям:")
    for email, stats in user_stats.items():
        print("Пользователь:", email)
        print("Изменено строк:", stats["lines_changed"])
        print("Количество коммитов:", stats["commits"])
        print("=" * 40)
