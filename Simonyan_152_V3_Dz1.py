#Ася Симонян, БКЛ-152-итал, Вариант 3
while True:
    print('hey you')
    a = input('please, choose any number you want, it\'s gonna be \'a\' ')
    b = input('please, choose another number, it\'s gonna be \'b\'')
    c = input('please, choose a number for the last time, it\'s gonna be \'c\'')

    if float(b) == 0:
        print('sorry, in this country you\'re not allowed to divide by zero')
        print('so you can\'t really have c as a remainder')
    elif float(a) % float(b) == float(c):
        print('if you divide a by b, you\'ll have c as a remainder')
    else:
        print('if you divide a by b, the remainder won\'t equal c')

    if float(a) * float(c) + float(b) == 0:
        print('c is the root of the equasion ax+b=0')
    else:
        print('c is not the root of the equasion ax+b=0')    
