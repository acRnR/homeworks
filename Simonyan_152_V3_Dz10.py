# Ася Симонян, БКЛ-152-итал, Вариант 3

import re

def add_to_file(result):
    f = open('В_ПредложномПадеже.txt', 'a', encoding = 'UTF-8')
    f.write(result)
    f.close()

def reads_file():
    f = open('rur.txt', 'r', encoding = 'UTF-8')
    string = f.read()
    f.close()
    return string

def find_collocation(string):
    res = re.findall(' въ [^ ]+?ѣ[ .,!?)]', string)
    for elem in res:
        elem = elem.strip(' .,!?)')
        add_to_file(elem + '\n')
    
def main():
    find_collocation(reads_file())

if __name__ == '__main__':
    main()
