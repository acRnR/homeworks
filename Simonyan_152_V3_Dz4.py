#Ася Симонян, БКЛ-152, вариант 3

spisok = []
while True:
    word = input('input any word: ')
    if word == '':
        break
    spisok.append(word)
spisok.reverse()
for slovo in spisok:
    print(slovo)    
