# ZADANIE 7
# var2.1
n = int(input('Введите кол-во элементов: '))
mas = []
for i in range(n):
    x = float(input())
    mas.append(x)

total = 0
for x in mas:
    total = total + x

sr = total / n

for i in range(n):
    if mas[i] == 0:
        mas[i] = sr
print(mas)

# var2.2
n = int(input('Введите кол-во элементов: '))
mas = []
for i in range(n):
    x = int(input())
    mas.append(x)

mas2 = []
mas3 = []

for x in mas:
    if x > 0:
        mas2.append(x)
    else:
        mas3.append(x)
print('Положительный массив', mas2)
print('Отрицательный массив', mas3)

# var3.2
mas = []
print('Введите 8 элементов: ')
for i in range(8):
    x = int(input())
    mas.append(x)
for i in range(8):
    if mas[i] < 15:
        mas[i] = mas[i] * 2
print(mas)

# var4.2
n = int(input('Введите кол-во элементов: '))
mas = []
for i in range(n):
    x = float(input())
    mas.append(x)
nech = []
for x in mas:
    if x % 2 != 0:
        nech.append(x)
n = sorted(nech)
if len(n) == 0:
    print('Нечетных чисел нет')
else:
    print(n[::-1])

# var5.2
mas = []
print('Введите 10 элементов: ')
for i in range(10):
    x = int(input())
    mas.append(x)

new_mas = []
for x in mas:
    if x not in new_mas:
        new_mas.append(x)
print(new_mas)

# var 6.2
mas = []
for i in range(10):
    x = int(input())
    mas.append(x)
total = 0
for x in mas:
    if x > 5:
        total = total + x
print(total)

# var 7.2
mas = []
print('Введите количество элементов: ')
n = int(input())
for i in range(n):
    x = int(input())
    mas.append(x)
min_i = 0
max_i = 0
for i in range(n):
    if mas[i] < mas[min_i]:
        min_i = i
    if mas[i] > mas[max_i]:
        max_i = i
p = mas[min_i]
mas[min_i] = mas[max_i]
mas[max_i] = p
print('Измененный массив: ', mas)

# var 8.2
mas = []
print('Введите количество элементов: ')
n = int(input())
for i in range(n):
    x = float(input())
    mas.append(x)
total = 0
for x in mas:
    total = total + x
sr = total/n
for i in range(n):
    if mas[i] == 0:
        mas[i] = sr
print('Измененный массив: ', mas)

# var 9.2
mas_A = []
mas_B = []

for i in range(10):
    x = int(input())
    mas_A.append(x)
print('Изначальный массив A: ', mas_A)
for i in range(10):
    x = int(input())
    mas_B.append(x)
print('Изначальный массив B: ', mas_B)
for i in range(10):
    p = mas_A[i]
    mas_A[i] = mas_B[i]
    mas_B[i] = p
print('Новый массив A: ', mas_A)
print('Новый массив B: ', mas_B)

# var 10.2
mas = []
for i in range(15):
    x = int(input())
    mas.append(x)
print('Изначальный массив: ', mas)
for i in range(15):
    if mas[i] < 10:
        mas[i] = 0
    elif mas[i] > 20:
        mas[i] = 1
print('Новый массив: ', mas)

# var 11.2
mas = []
print('Введите количество элементов: ')
n = int(input())
for i in range(n):
    x = int(input())
    mas.append(x)
new_mas = []
for x in mas:
    if x % 2 == 0 and x < 10:
        new_mas.append(x)
if len(new_mas) == 0:
    print('Таких чисел нет')
else:
    new_mas.sort()
print(new_mas)

# var 12.2
mas_A = []
mas_B = []

for i in range(10):
    x = int(input())
    mas_A.append(x)
print('Изначальный массив A: ', mas_A)
for i in range(10):
    x = int(input())
    mas_B.append(x)
print('Изначальный массив B: ', mas_B)
for i in range(10):
    p = mas_A[i]
    mas_A[i] = mas_B[i]
    mas_B[i] = p
print('Новый массив A: ', mas_A)
print('Новый массив B: ', mas_B)

# var 13.2
mas = []
for i in range(8):
    x = int(input())
    mas.append(x)
for i in range(8):
    if mas[i] < 15:
        mas[i] = mas[i] * 2
print(mas)

# var 14.2
mas = []
for i in range(10):
    x = int(input())
    mas.append(x)
total = 0
for x in mas:
    total = total + x
    sr = total/10
for i in range(10):
    if mas[i] > sr:
        mas[i] = 1
print(mas)

# var 15.2
mas = []
print('Введите количество элементов: ')
n = int(input())
for i in range(n):
    x = int(input())
    mas.append(x)
new_mas = []
for x in mas:
    if x % 2 != 0:
        new_mas.append(x)
if len(new_mas) == 0:
    print('Таких чисел нет')
else:
    new_mas.sort()
    new_mas = new_mas[::-1]
print(new_mas)