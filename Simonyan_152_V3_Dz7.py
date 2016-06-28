#Ася Симонян, БКЛ-152-ит, 3 вариант

import random

def create_dictionary():
    f = open('tabletry.csv', 'r', encoding = 'UTF-8')
    a = ()
    b = []
    for line in f:
        line = line.strip('\ufeff\n')
        a = tuple(line.split(';'))
        b.append(a)
    d = dict(b)
    f.close()
    return d

def one_turn(d, hint, n_attempts):
    first_guess = input('Угадайте слово, стоящее на месте пропуска (следите за орфографией):\n' + hint + '\n')
    if first_guess == d[hint]:
        what_next = input('Поздравляем! Вы победили!\nЕсли хотите сыграть еще, введите любой знак/послеловательность знаков.\nЕсли хотите выйти из игры, ничего не вводя, нажмите enter')
    else:
        while n_attempts != 0:
            guess = input('Нет, попробуйте еще раз.\nПопыток осталось: ' + str(n_attempts) + '\n(Если хотите сдаться, ничего не вводя, нажмите enter):\n')  
            if guess == d[hint]:
                what_next = input('Поздравляем! Вы победили!\nЕсли хотите сыграть еще, введите любой знак/последовательность знаков.\nЕсли хотите выйти из игры, ничего не вводя, нажмите enter'+'\n----------------------------------------------------------\n')
                break
            elif guess == '':
                n_attempts = 0
            else:
                n_attempts -= 1
    if n_attempts == 0:
        what_next = input('К сожалению, вы проиграли. Это было слово \'' + d[hint] +'\'\nЕсли хотите сыграть еще, введите любой знак/последовательность знаков.\nЕсли хотите выйти из игры, ничего не вводя, нажмите enter\n----------------------------------------------------------\n')
    return what_next

def the_game():
    print('Здравствуйте! Начинаем игру.')
    while True:
        d = create_dictionary()
        hint = random.choice(list(d.keys()))
        n_attempts = len(hint) - 5
        what_next = one_turn(d, hint, n_attempts)
        if what_next == '':
            print('До свидания.')
            break
def main():
    the_game()

if __name__ == '__main__':
    main()
