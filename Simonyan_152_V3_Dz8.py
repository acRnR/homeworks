#Ася Симонян, БКЛ-152-ит, 3 вариант

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

def array(path):
    file = open(path, "r", encoding = 'UTF-8')
    m = []
    for string in file:
        words = string.split(' ')
        for word in words:
            word = word.strip('.,!?^$@#:;_- []()\|/\n\ufeff')
            word = word.lower()
            m.append(word)        
    file.close()
    return m

def print_words(arr):
    array = []
    for elem in arr:
        if elem in array:
            continue
        else:
            array.append(elem)
    for word in array:
        print(word)
        
def all_word_forms():
    arr = []
    words = array(opens_file())
    for word in words:
        check1 = re.search('программир(у(я.*|ю.*|е.*)|ова(ть.*|л.*|вш.+))', word)
        check2 = re.search('.+программир(у(я.*|ю.*|е.*)|ова(ть.*|л.*|вш.+))', word)
        if check1 != None and check2 == None:
            arr.append(word)
        else:
            continue
    print_words(arr)
            
def main():
    all_word_forms()

if __name__ == '__main__':
    main()
