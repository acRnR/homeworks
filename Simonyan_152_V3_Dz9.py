# Ася Симонян, БКЛ-152-итал, Вариант 3

import re

def opens_file():
    some_f = input('Впишите полное название файла, не забудьте про расширение\n(пример: d:\главная_папка\дочерняя_папка\файл_в_дочерней_папке.txt):\n')
    while True:
        try:
            f = open(some_f, 'r')
        except FileNotFoundError:
            some_f = input('Такого файла нет. Впишите полное название файла, не забудьте про расширение\n(пример: d:\главная_папка\дочерняя_папка\файл_в_дочерней_папке.txt):\n')
        else:
            break
    return some_f

def add_to_file(string):
    f = open('Количество преподавателей в вузе.txt', 'a')
    f.write(string)
    f.close()

def reads_file(path):
    f = open(path, 'r', encoding = 'UTF-8')
    strings = f.readlines()
    f.close()
    return strings

def find_number(strings):
    i = 0
    while i < len(strings):
        if '\">Преподаватели</th>' in strings[i]:
            try:
                res = re.search('<p>([^#&;]+?)<', strings[i + 2])
                number = res.group(1) 
            except AttributeError:
                number = ''
            break
        else:
            i += 1
    add_to_file(number + '\n')
                
    
def main():
    find_number(reads_file(opens_file()))

if __name__ == '__main__':
    main()
