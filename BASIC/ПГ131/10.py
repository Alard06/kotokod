def check(password, condition):
    count = 0
    for i in password:
        if i in condition:
            count += 1
    return count


def check2(password):
    max_duplicate = 1
    temp = 1
    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            temp += 1
            if temp > max_duplicate:
                max_duplicate = temp
        else:
            pass
    if max_duplicate >= 5:
        return False
    return True


while True:
    cat = str(input('Введи значение: '))
    count_numbers = 0
    count_letters = 0
    if check2(cat):
        print('Не хватает дуб')
    elif not (len(cat) >= 5):
        print(f'Не хватает символов: {5 - len(cat)}')
    elif check(cat, '1234567890') < 10:
        print('Меньше 10')
    elif check(cat, '!@#$%^&*()') < 5:
        print('Меньше 5')
    elif check(cat, 'ABRA') < 2:
        print('Меньше 2')
