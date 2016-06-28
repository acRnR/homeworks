
# Ася Симонян, БКЛ-152, ДЗ-3, Вариант 3

print('Hello!')

while True:
    
    n = input('Please input a NATURAL NUMBER (to stop just press enter): ')
    
    if n == '':
        break


    while True:
        try:
            i = int(n)
        except ValueError:
            n = input('Please input a NATURAL NUMBER (to stop just press enter): ')
            if n == '':
                break
        else:
            break         
    if n == '':
        break

    i_2 = i
    i_3 = i
    
    for num in range(i):
        output = ''
        i_2 = i_3
        for sym in range(i):
            output += str(i_2)
            if i > 5 and i_2 != i_3 - i: # чтобы двузначные числа не сливались
                output += ' '
                if i_2 < 10: # чтобы выходил красивый прямоугольник, а не кривое непонятно что
                    output += ' '
            i_2 -= 1
        print(output)
        i_3 += 1
