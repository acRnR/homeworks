#Simonyan Anna Var 1

#1

def reads_n_prints():
    f = open('shtirlits.txt', 'r', encoding = 'UTF-8')
    #попробовать for line in f
    arr = f.readlines()
    for line in arr:
        if len(line) > 20:
            print(line)
    f.close()
            
#2

def reads_file():
    f = open('shtirlits.txt', 'r', encoding = 'UTF-8')
    text = f.read()
    text_as_list = list(text.lower())
    arr = list(enumerate(text_as_list))
    f.close()
    return arr

def ciphers_n_prints():
    arr = reads_file()
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for letter in alf:
        for item in reversed(arr):
            if item[1] == letter:
                print(letter.upper() + letter + '\t' + str(item[0]))
                break
#3

def ciphers():
    arr = reads_file()
    ciph_arr = []
    code = ()
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for letter in alf:
        for item in reversed(arr):
            if item[1] == letter:
                code = (letter, item[0])
                ciph_arr.append(code)
                break
    return ciph_arr

def asks_for_word():
    word = input('Введите слово, которое хотите зашифровать.\nЧтобы выйти из программы, ничего не вводите и нажмите enter:\n')
    word = word.lower()
    return word

def codes():
    ciph_arr = ciphers()
    while True:
        word = asks_for_word()
        #word = input('Введите слово, которое хотите зашифровать.\nЧтобы выйти из программы, ничего не вводите и нажмите enter:\n')
        if word == '':
            break
        #word = word.lower()
        new_w = ''
        for let in word:
            i = 0
            for items in ciph_arr:
                while i < 33:
                    if let == ciph_arr[i][0]:
                        new_w += str(ciph_arr[i][1]) + ' '
                        break
                    else:
                        i += 1
                    break
                continue
        print(new_w[0:0:-33])
    
def main():
    codes()
    #reads_n_prints()
    #ciphers_n_prints()
if __name__ == '__main__':
    main()



    
