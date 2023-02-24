a = int(input('введите трехзначное число: '))
summa = 0
x = a % 10
summa = summa + x
x = a // 100
summa = summa + x
x = (a // 10) % 10
summa = summa + x
print(summa)