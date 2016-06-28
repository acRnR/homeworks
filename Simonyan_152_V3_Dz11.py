#Ася Симонян, БКЛ-152-ит, Вариант 3

import re

def reads_file():
    f = open('yazyk.txt', 'r', encoding = 'UTF-8')
    text = f.read()
    f.close()
    return text

def new_file(result):
    f = open('shashlyk.txt', 'w', encoding = 'UTF-8')
    f.write(result)
    f.close()
    
def the_magic(text):
    law_text = re.sub('язык((а(м(и)?|х)?|и|о(в|м)|е|у)|( |\.|,|\)|:|;|\?|!|\n|\t\|»|-))', r'шашлык\1', text)
    high_text = re.sub('Язык((а(м(и)?|х)?|и|о(в|м)|е|у)|( |\.|,|\)|:|;|\?|!|\n|\t\|»|-))', r'Шашлык\1', law_text)
    return high_text

def main():
    new_file(the_magic(reads_file()))

if __name__ == '__main__':
    main()
