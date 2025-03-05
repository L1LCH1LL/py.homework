# Открываем файл для чтения
philosophical_text = open("zen.txt", "r")
# Считываем все строки в список
lines = philosophical_text.readlines()
# Закрываем файл после чтения
philosophical_text.close()

for line in reversed(lines):
    print(line.strip())