import subprocess

# Функция для выполнения команды git config --global --list
def git_config_list():
    # Выполняем команду и сохраняем результат
    result = subprocess.run(["git", "config", "--global", "--list"], capture_output=True, text=True)
    
    # Выводим результат выполнения команды
    print(result.stdout)

# Вызываем функцию
git_config_list()
