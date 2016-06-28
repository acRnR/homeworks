#Ася Симонян, БКЛ-152-ит, вариант 3

#все слова в файлах загружены из словаря А.А.Зализняка и обработаны частично с
#помощью питона, частично в нотпад++(некоторые пометы не соответствуют тем, что
#в словаре, т.к. я соединила некоторые классы, как удобнее для данного задания)

import random

def open_choose_split(name):
    #открывает файл с нужной частью речи, выбирает строчку и делает из нее список
    f = open(name, 'r')
    spisok = f.readlines()
    choose = random.choice(spisok)
    spl = choose.split(' ')
    return spl

def close_all(name):
    #закрывает файл
    f = open(name, 'r')
    f.close()
    
def adv():
    #возвращает случайное наречие
    choice = open_choose_split('adverbs_6.txt')
    close_all('adverbs_6.txt')
    return choice[0].strip('\n')   

def v_indicative():
    #возвращает слуайный глагол в изъявительном наклонении, в 3л. ед.ч.
    v = ''
    while v == '':
        choice = open_choose_split('vverbs_6.txt')
        word = choice[0] + ' '
        group = choice[1]
        v = flex_for_ind(word, group)
    close_all('vverbs_6.txt')
    return v

def v_imperative():
    #возвращает случайный глагол в повелительном наклонении, в ед.ч.
    v = ''
    while v == '':
        choice = open_choose_split('vverbs_6.txt')
        word = choice[0] + ' '
        group = choice[1]
        v = flex_for_imp(word, group)
    close_all('vverbs_6.txt')
    return v
    
def the_nominative():
    #возвращает словосочетание "прил. + сущ." в Им.п.
    choice = open_choose_split('nnoouns_6.txt')
    noun = choice[0]
    conj = choice[1]
    a = the_adj_nom(conj)
    close_all('nnoouns_6.txt')
    return a + ' ' + noun

def the_accusative():
    #возвращает словосочетание "прил. + сущ" в Вин.п.
    n = ''
    while n == '':
        choice = open_choose_split('nnoouns_6.txt')
        word = choice[0] + '@'
        conj = choice[1]
        if conj.startswith('МО') or (conj.startswith('Ж') and conj != 'Ж0\n'):
            n = noun_acc(word, conj)
        else:
            n = word
    a = the_adj_acc(conj)
    close_all('nnoouns_6.txt')
    return a + ' ' + n

def the_adj_nom(gender):
    #возвращает словосочетание "прил. + сущ" в Им.п.
    a = ''
    while a == '':
        choice = open_choose_split('adjj_6.txt')
        #print(choice)
        word = choice[0]
        con = choice[1]
        if gender.startswith('М'):
            a = word
        else:
            a = adj_nom(word, con, gender)
    close_all('adjj_6.txt')
    return a


def the_adj_acc(gender):
    #возвращает случайное прилагательное в Вин.п., по роду согласованное с выбранным существительным
    a = ''
    while a == '':
        choice = open_choose_split('adjj_6.txt')
        word = choice[0]
        con = choice[1]
        if gender.startswith('МО') or gender.startswith('Ж'): 
            a = adj_acc(word, con, gender)
        elif gender.startswith('С'):
            a = adj_nom(word, con, gender)
        else:
            a = word
    close_all('adjj_6.txt')
    return a

def adj_nom(word, con, gen):
    #возвращает случайное прилагательное в Им.п.(или В.п. для неодуш.), по роду согласованное с выбранным существительным
    h = conj_1(word, con, gen, 'C', 'ое')
    if h == '':
        h1 = conj_1(word, con, gen, 'Ж', 'ая')
        if h1 == '':
            h2 = conj_2(word, con, gen, 'C', 'ее', 'ее')
            if h2 == '':
                h3 = conj_2(word, con, gen, 'Ж', 'яя', 'ая')
                return h3
            else:
                return h2
        else:
            return h1
    else:
        return h

def adj_acc(word, con, gen):
    #возвращает прилагательное с необходимым окончанием
    h = conj_1(word, con, gen, 'МО', 'ого')
    if h == '':
        h1 = conj_1(word, con, gen, 'Ж', 'ую')
        if h1 == '':
            h2 = conj_2(word, con, gen, 'МО', 'его', 'его')
            if h2 == '':
                h3 = conj_2(word, con, gen, 'Ж', 'юю', 'ую')
                return h3
            else:
                return h2
        else:
            return h1
    else:
        return h
    
def conj_1(word, con, gen, g, a1):
    #"подбирает" окончание  для  прилагательного
    if con.startswith('1А\n') and gen.startswith(g):
        word = word.replace('ый', a1)
        return word
    if con.startswith('1В?') and gen.startswith(g):
        word = word.replace('ой', a1)
        return word
    if con.startswith('3А') and gen.startswith(g):
        word = word.replace('ий', a1)
        return word
    else:
        return ''
    
def conj_2(word, con, gen, g, a2, a4):
    #"подбирает" окончание  для  прилагательного
    if con.startswith('2А\n') and gen.startswith(g):
        word = word.replace('ий', a2)
        return word
    if con.startswith('4А\n') and gen.startswith(g):
        word = word.replace('ий', a4)
        return word
    else:
        return ''
    
    
def noun_acc(word, conj):
    #возвращает существительное с необходимым окончанием для Вин.п.
    if conj == 'Ж1А\n':
        w = word.replace('а@', 'у')
        return w
    if conj == 'Ж2А\n':
        w = word.replace('я@', 'ю')
        return w
    if conj == 'МО2А\n' and word[-2] == 'ь':
        w = word.replace('ь@', 'я')
        return w
    if conj == 'МО2А\n' and word[-2] == 'й':
        w = word.replace('й@', 'я')
        return w  
    if conj == 'МО1А\n':
        w = word.replace('@', 'а')
        return w
    if conj == 'МО5*А\n':
        w = word.replace('ец@','ца')
        return w
    else:
        return ''
            
def flex_for_ind(word, group):
    #возвращает глагол с необходимым окончанием для изъяв.накл, 3ед.
    v1 = v_group1(word, group, 'ет', 'т')
    if v1 == '':
        v2 = v_group2(word, group, '')
        if v2 == '':
            v3 = v_group3(word, group, 'ет', 'нет', 'ьет')
            if v3 == '':
                v4 = v_group4(word, group, 'ет', 'вет', 'ет')
                return v4
            else:
                return v3
        else:
            return v2
    else:
        return v1    
                    
def flex_for_imp(word, group):
    #возвращает глагол с необходимым окончанием для повел.накл, ед.
    n1 = v_group1(word, group, 'й', '')
    if n1 == '':
        n3 = v_group3(word, group, 'и', 'нь', 'ей')
        if n3 == '':
            n4 = v_group4(word, group, 'ри', 'ви', 'и')
            return n4
        else:
            return n3
    else:
        return n1
    
def men_u(slovo):
    #делает дополнительную замену для слов на -овать и -евать
    if slovo.endswith('левать '):
        s = slovo.replace('левать ','лють ')
    if slovo.endswith('овать '):
        s = slovo.replace('овать ','уть ')
    else:
        s = slovo.replace('евать ', 'уть ')
    return s
            
def v_group1(word, group, a1, b4):
    #"подбирает" окончание для глагола
    if group.startswith('1А'):
        word = word.replace('ть ', a1)
        return word
    if group == '2А\n':
        word = men_u(word)
        word = word.replace('ть ', a1)
        return word
    if group == '12А\n':
        if word[-4] == 'ы':
            word = word.replace(word[-4],'о')
        w = word.replace('ть ', a1)
        return w
    if group.startswith('4В'):
        word = word.replace('ть', b4)
        return word
    else:
        return ''
    
def v_group2(word, group, a45):
    #"подбирает" окончание для глагола  (у этих двух групп глаголов очень разные
    if group == '4А\n':                 #и странные формы императива, поэтому 
        word = word.replace('ь ', a45)  #из них программа делает только индикатив)
        return word
    if group.startswith('5А'):
        w = word.replace(word[-4],'и')
        w = w.replace('ь ', a45)
        return w
    else:
        return ''
    
def v_group3(word, group, a3, a15, b11):
    #"подбирает" окончание для глагола
    if group.startswith('3А'):
        word = word.replace('уть ', a3)
        return word
    if group.startswith('15А'):
        word = word.replace('ть', a15)
        return word
    if group.startswith('11В'):
        word = word.replace('ить ', b11)
        return word
    else:
        return ''
    
def v_group4(word, group, b9, b16, c10):
    #"подбирает" окончание для глагола
    if group == '9В\n':
        word = word.replace('ереть', b9)
        return word
    if group == '16В\n':
        word = word.replace('ть', b16)
        return word
    if group == '10С\n':
        word = word.replace('оть', c10)
        return word
    else:
        return ''
    
def first_up(word):
    #возвращает слово (аргумент), написанное с заглавной буквы
    word = list(word)
    cap = word[0]
    word[0] = cap.upper()
    s2 = ''.join(word)
    return s2


def utverditelnoe():
    #возвращает утвердительное предложение
    subj = the_nominative().strip()
    sbj = first_up(subj)
    adverb = adv()
    verb = v_indicative()
    obj = the_accusative().strip(' ')
    return sbj + ' ' + adverb + ' ' + verb + ' ' + obj + '.'

def otrits_1():
    #возвращает предложение с отрицанием на наречии 
    subj = the_nominative().strip()
    sbj = first_up(subj)
    adverb = adv()
    verb = v_indicative()
    obj = the_accusative().strip(' ')
    stri = sbj + ' не ' + adverb + ' ' + verb + ' ' + obj + '.'
    return stri

def otrits_2():
    #возвращает предложение с отрицанием на предикате
    subj = the_nominative().strip()
    sbj = first_up(subj)
    adverb = adv()
    verb = v_indicative()
    obj = the_accusative().strip(' ')
    stri = sbj + ' не ' + verb + ' ' + adverb + ' ' + obj + '.'
    return stri

def otrits_3():
    #возвращает предложение с отрицанием на субъекте
    subj = the_nominative().strip()
    adverb = adv()
    verb = v_indicative()
    obj = the_accusative().strip(' ')
    stri = 'Не ' + subj + ' ' + adverb + ' ' + verb + ' ' + obj + '.'
    return stri

def otrits_4():
    #возвращает предложение с отрицанием на объекте
    subj = the_nominative().strip(' ')
    sbj = first_up(subj)
    adverb = adv()
    verb = v_indicative().strip(' ')
    obj = the_accusative().strip(' ')
    stri = sbj + ' ' + adverb + ' ' + verb + ' не ' + obj + '.'
    return stri

def otritsatelnoe():
    #возвращает случайное отрицательное предложение
    vybor = random.randint(1, 4)
    if vybor == 1:
        op = otrits_1()
    if vybor == 2:
        op = otrits_2()
    if vybor == 3:
        op = otrits_3()
    if vybor == 4:
        op = otrits_4()
    return op

def uslovie():
    #возвращает часть условного или вопросительного предложения
    vybor = random.randint(1, 2)
    if vybor == 1:
        op = utverditelnoe()
    if vybor == 2:
        op = otritsatelnoe()
    return op

def uslovnoe():
    #возвращает случайное условное предложение
    usl = uslovie().lower()
    us2 = uslovie().lower()
    pridat = usl.replace('.', ',') 
    stri = 'Если '+ pridat + ' то ' + us2
    return stri

def pobuditelnoe():
    #возвращает побудительное предложение
    adverb = adv()
    ab = first_up(adverb)
    verb = v_imperative().strip(' ')
    obj = the_accusative().strip(' ')
    stri = ab + ' ' + verb + ' ' + obj + '.'
    return stri

def voprositelnoe():
    #возвращает случайное вопросительное предложение
    ques = ['Когда ', 'Почему ', 'Зачем ', 'За что ', 'Как ', 'Где ']
    vopr = random.choice(ques)
    usl = uslovie()
    predl = usl.lower()
    stri = vopr + predl.replace('.', '?')
    return stri

def the_text():
    #возвращает случайный текст, удовлетворяющий условию домашнего задания
    text = [utverditelnoe(), otritsatelnoe(), uslovnoe(), pobuditelnoe(), voprositelnoe()]
    random.shuffle(text)
    tadaa = ' '.join(text)
    return tadaa

def main():
    #собственно, вот и все :)
    print(the_text())

if __name__ == '__main__':
    main()


