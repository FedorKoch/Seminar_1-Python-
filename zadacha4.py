n = int(input('Введите длину шоколадки: '))
m = int(input('Введите ширину шоколадки: '))
k = int(input('Введите количество плиток, которые нужно отрезать: '))
if k % n == 0 or k % m ==0:
    print('Yes')
else:
    print('No')