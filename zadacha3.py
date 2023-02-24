a = int(input('Введите шестизначный номер билета: '))

b = a % 1000
summa1 = 0
x = b % 10
summa1 = summa1 + x
x = b // 100
summa1 = summa1 + x
x = (b // 10) % 10
summa1 = summa1 + x

c = a // 1000
summa2 = 0
x = c % 10
summa2 = summa2 + x
x = c // 100
summa2 = summa2 + x
x = (c // 10) % 10
summa2 = summa2 + x

if summa1 == summa2:
    print('yes')
else:
    print('no')