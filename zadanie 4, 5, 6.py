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


# ZADANIE 5
# z1
N = int(input())
i = 1
while i * i <= N:
    print(i * i)
    i += 1

# z2
n = int(input())
d = 2
while n % d != 0:
    d += 1
print(d)


# z3
n = int(input())
power = 1
exponent = 0
while power * 2 <= n:
    power *= 2
    exponent += 1
print(exponent, power)

# z4
x = float(input())
y = float(input())
day = 1
distance = x
while distance < y:
    distance *= 1.10
    day += 1
print(day)

# z5
c = 0
while True:
    num = int(input())
    if num == 0:
        break
    c += 1
print(c)

# z6
total = 0
c = 0
while True:
    num = int(input())
    if num == 0:
        break
    total += num
    c += 1
print(total / c)

# z7
c = 0
prev = int(input())
if prev != 0:
    while True:
        curr = int(input())
        if curr == 0:
            break
        if curr > prev:
            c += 1
        prev = curr
print(c)

# z8
prev = int(input())
max_len = 0
current_len = 1
while prev != 0:
    curr = int(input())
    if curr == 0:
        if current_len > max_len:
            max_len = current_len
        break
    if curr == prev:
        current_len += 1
    else:
        if current_len > max_len:
            max_len = current_len
        current_len = 1
        prev = curr
print(max_len)


# ZADANIE 6
# variant 12
s = input("Введите строку: ")
for p in '.,!?;:-()"\'':
    s = s.replace(p, ' ')
for word in s.split():
    if word[-1] == 'я' or word[-1] == 'Я':
        print(word)