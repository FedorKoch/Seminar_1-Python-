a = int(input('Введите число журавликов: '))
if  a % 6 == 0:
    x = a // 6
    print('Петя сделал: ', x)
    print('Сережа сделал: ', x)
    print('Катя сделала: ', 4*x)
else:
    print('Дети врут')   