#Ася Симонян, БКЛ-152, 3 Вариант
#ДЗ-2

print('Hello!')

while True:
    
    original_text = input('Please input any text you like: ')
    count = 0

    if original_text == '':
        break
    elif len(original_text) < 4:
        continue
    else:
        for sym in original_text:
            if count < 2:
                count += 1
                continue
            if count == len(original_text) - 2:
                break
            count += 1
            print(sym)
