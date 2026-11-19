# ZADANIE 8
# var2.1
def f(mas):
    s = sum(mas)
    sr = s / len(mas)
    return s, sr

for i in range(3):
    m = int(input('Размер массива(не более 15): '))
    mas = []
    for j in range(m):
        mas.append(int(input('Элемент: ')))
    s, sr = f(mas)
    print('Сумма =', s, 'Среднее =', sr)

# var2.2
def S(a, b):
    return a * b

for i in range(3):
    a = float(input('Сторона 1: '))
    b = float(input('Сторона 2: '))
    print('Площадь =', S(a, b))

# var2.3
def sort_words(text):
    words = text.split()
    result = ''
    for w in words:
        sorted_letters = sorted(w)
        word_sorted = ''.join(sorted_letters)
        result = result + word_sorted + ' '
    return result
s = input('Строка: ')
print(sort_words(s))

# var2.4
import math
def inside(x, y, a, b, r):
    d = math.hypot(x - a, y - b)
    return d < r
a = float(input('a: '))
b = float(input('b: '))
r = float(input('R: '))
points = []
for name in ['P', 'F', 'L']:
    x = float(input(name + '.x: '))
    y = float(input(name + '.y: '))
    points.append((name, x, y))
count = 0
for p in points:
    name = p[0]
    x = p[1]
    y = p[2]
    if inside(x, y, a, b, r):
        print('Точка', name, 'внутри')
        count = count + 1
    else:
        print('Точка', name, 'снаружи')
print('Внутри:', count)

# var2.5
def d(n):
    res = []
    for d in range(1, n + 1):
        if n % d == 0:
            res.append(d)
    return res

n = int(input('Число: '))
print(*d(n))

# var2.6
import math

def tr(a, b, c):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
d = float(input('d: '))
diag = float(input('Диагональ: '))

S1 = tr(a, b, diag)
S2 = tr(c, d, diag)
print('Площадь =', S1 + S2)

# var2.7
def f(n):
    r = ''
    while n > 0:
        r = str(n % 8) + r
        n = n // 8
    while len(r) < 10:
        r = '0' + r
    return r
s = int(input('Число: '))
print(f(s))

# var2.8
def zam(X):
    X[0], X[-1] = X[-1], X[0]
m = int(input('Длина массива: '))
A = []
for i in range(m):
    A.append(int(input('Элемент: ')))
print('Было:', A)
zam(A)
print('Стало:', A)

# var2.9
def f(mas):
    p = 1
    for x in mas:
        p = p * x
    sr = sum(mas) / len(mas)
    return p, sr
for i in range(3):
    m = int(input('Размер массива: '))
    mas = []
    for j in range(m):
        mas.append(int(input('Элемент: ')))
    p, sr = f(mas)
    print('Произведение =', p, 'Среднее =', sr)

# var2.10
def reverse_words(text):
    words = text.split()
    words.reverse()
    return ' '.join(words)
s = input('Строка: ')
print(reverse_words(s))

# var2.11
def find_max(M):
    mi = 0
    mj = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] > M[mi][mj]:
                mi = i
                mj = j
    return mi, mj

def input_matrix(name):
    r = int(input(name + ': строк: '))
    c = int(input(name + ': столбцов: '))
    M = []
    for i in range(r):
        st = []
        for j in range(c):
            st.append(int(input('эл: ')))
        M.append(st)
    return M

A = input_matrix('A')
B = input_matrix('B')

ia, ja = find_max(A)
ib, jb = find_max(B)

p = A[ia][ja]
A[ia][ja] = B[ib][jb]
B[ib][jb] = p

print('A:', A)
print('B:', B)

# var2.12
import math

def median(a, b, c):
    m = 0.5 * math.sqrt(2 * b * b + 2 * c * c - a * a)
    return m

a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))

ma = median(a, b, c)
mb = median(b, a, c)
mc = median(c, a, b)
print('Медианы исходного треугольника:', ma, mb, mc)

m1 = median(ma, mb, mc)
m2 = median(mb, ma, mc)
m3 = median(mc, ma, mb)
print('Медианы нового треугольника:', m1, m2, m3)

# var2.13
import math

def angle(x, y):
    return math.atan2(y, x)

names = ['X', 'Y', 'Z']
xs = []
ys = []

for name in names:
    x = float(input(name + '.x: '))
    y = float(input(name + '.y: '))
    xs.append(x)
    ys.append(y)

min_i = 0
min_ang = abs(angle(xs[0], ys[0]))

for i in range(1, 3):
    a = abs(angle(xs[i], ys[i]))
    if a < min_ang:
        min_ang = a
        min_i = i
print('Точка', names[min_i], '(', xs[min_i], ',', ys[min_i], ')')
print('Угол =', math.degrees(angle(xs[min_i], ys[min_i])))

# var2.14
import math

def dist(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

names = ['X', 'Y', 'Z', 'P']
xs = []
ys = []

for name in names:
    x = float(input(name + '.x: '))
    y = float(input(name + '.y: '))
    xs.append(x)
    ys.append(y)

max_dist = -1
best_i = 0
best_j = 0

for i in range(4):
    for j in range(i + 1, 4):
        d = dist(xs[i], ys[i], xs[j], ys[j])
        if d > max_dist:
            max_dist = d
            best_i = i
            best_j = j
print('Макс. расстояние = ', max_dist)
print('Между точками', names[best_i], 'и', names[best_j])

# var2.15
import math

def dist(x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    return math.sqrt(dx * dx + dy * dy + dz * dz)

names = ['X', 'Y', 'Z', 'T']
xs = []
ys = []
zs = []

for name in names:
    x = float(input(name + '1: '))
    y = float(input(name + '2: '))
    z = float(input(name + '3: '))
    xs.append(x)
    ys.append(y)
    zs.append(z)

min_dist = 10**9
best_i = 0
best_j = 0

for i in range(4):
    for j in range(i + 1, 4):
        d = dist(xs[i], ys[i], zs[i], xs[j], ys[j], zs[j])
        if d < min_dist:
            min_dist = d
            best_i = i
            best_j = j
print('Мин. расстояние =', min_dist)
print('Между точками', names[best_i], 'и', names[best_j])