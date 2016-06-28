# Ася Симонян, БКЛ-152-итал, Вариант 3

import os
import re

def listof_ext():
    ext_list = []
    for root, dirs, files in os.walk('.'):
        for fl in files:
            res = re.search('.+\.([^.]+)', fl)
            if res != None:
                ext = res.group(1)
                ext_list.append(ext)
    return ext_list

def mostof_ext(lst):
    d = {}
    for el in lst:
        a = lst.count(el)
        d[a] = el
    print('В этих папках чаще всего встречаются файлы с расширением «' + d[max(d)] + '».')
    
def main():
    mostof_ext(listof_ext())

if __name__ == '__main__':

    main()
        
