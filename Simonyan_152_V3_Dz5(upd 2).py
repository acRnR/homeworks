#Ася Симонян, БКЛ-152-ит, вариант 3

some_f = input('Впишите полное название файла, не забудьте про расширение\n(пример: d:\главная_папка\дочерняя_папка\файл_в_дочерней_папке.txt):\n')

while True:
    try:
        f = open(some_f, 'r')
    except FileNotFoundError:
        some_f = input('Такого файла нет. Впишите полное название файла, не забудьте про расширение\n(пример: d:\главная_папка\дочерняя_папка\файл_в_дочерней_папке.txt):\n')
    else:
        break 

len_1 = 0
len_3 = 0
symbols = ['.', ',', ':', ';', '\'', '-', '?', '!',  '>', '<']

for line in f:
    new_l = line.split()
    for word in new_l:
        length = len(word)
        for sym in symbols:
            if word.endswith(sym):
                length = len(word) - 1
        if length == 1:
            len_1 += 1
        if length == 3:
            len_3 += 1
f.close()
if len_1 == 0:
    print('В данном тексте нет слов длины 1.')
else:
    answer = float(len_3 / len_1)
    if len_3 % len_1 == 0:
        answer = int(len_3 / len_1)
        if answer == 1:
            print('Слов длины 3 столько же, сколько и слов длины 1.')
        elif answer < 5 and answer > 1:
            print('Слов длины 3 в ' + str(answer) + ' раза больше, чем слов длины 1.')
    else:
        print('Слов длины 3 в ' + str(answer) + ' раз больше, чем слов длины 1.')
