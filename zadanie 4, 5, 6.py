# ZADANIE 4
# z1
A = int(input("Введите A: "))
B = int(input("Введите B: "))
for i in range(A, B + 1):
    print(i)

# z2
A = int(input("Введите A: "))
B = int(input("Введите B: "))
if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)

# z3
A = int(input("Введите A: "))
B = int(input("Введите B: "))
for i in range(A, B - 1, -1):
    if i % 2 != 0:
        print(i)

# z4
N = int(input("Введите количество чисел: "))
total = 0
for _ in range(N):
    total += int(input())
print("Сумма:", total)

# z5
n = int(input("Введите n: "))
total = 0
for i in range(1, n + 1):
    total += i ** 3
print("Сумма кубов:", total)

# z6
n = int(input("Введите n: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

# z7
n = int(input("Введите n: "))
total = 0
fact = 1
for i in range(1, n + 1):
    fact *= i
    total += fact
print("Сумма факториалов:", total)

# z8
n = int(input("Введите n: "))
if n <= 9:
    for i in range(1, n + 1):
        step = ''
        for j in range(1, i + 1):
            step += str(j)
        print(step)
else:
    print('Ошибка')

# z9
N = int(input("Введите количество чисел Фибоначчи: "))
a, b = 0, 1
total = 0
for _ in range(N):
    total += a
    a, b = b, a + b
print("Сумма:", total)

# z10
N = int(input("Введите количество чисел Фибоначчи: "))
K = int(input("Введите порядковый номер начала: "))
a, b = 1, 1
total = 0
for i in range(1, N + K):
    if i >= K:
        total += a
    a, b = b, a + b
print("Сумма:", total)