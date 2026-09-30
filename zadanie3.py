# ЗАДАЧА 1
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)


# ЗАДАЧА 2
a = float(input())
b = float(input())
pl = 0.5 * a * b
print(pl)


# ЗАДАЧА 3
n = int(input())
minutes_in_day = 24 * 60
n = n % minutes_in_day
hours = n // 60
minutes = n % 60
print(hours, minutes)


# ЗАДАЧА 4
# a = расстояние между рядами
# b = расстояние между дырочками в ряду
# l = длина свободного конца шнурка
# N = количество дырочек в каждом ряду

def shoelace_length(a, b, l, N):
    # Диагональные переходы между рядами: 2*N - 1
    # Горизонтальные участки в двух рядах: 2 * (N - 1) * b
    # Свободные концы: 2 * l
    length = (2 * N - 1) * a + 2 * (N - 1) * b + 2 * l
    return length

a = int(input())
b = int(input())
l = int(input())
N = int(input())
print(shoelace_length(a, b, l, N))


# ЗАДАЧА 5
def minn(a, b, c):
    return min(a, b, c)

a = int(input())
b = int(input())
c = int(input())
print(minn(a, b, c))


# ЗАДАЧА 6
def same_color(x1, y1, x2, y2):
    return "Да" if (x1 + y1) % 2 == (x2 + y2) % 2 else "Нет"

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(same_color(x1, y1, x2, y2))


# ЗАДАЧА 7
def v_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Да")
    else:
        print("Нет")

year = int(input())
v_year(year)


# ЗАДАЧА 8
def match(a, b, c):
    if a == b == c:
        print(3)
    elif a == b or b == c or a == c:
        print(2)
    else:
        print(0)

a = int(input())
b = int(input())
c = int(input())
match(a, b, c)


# ЗАДАЧА 9
def chocolate(n, m, k):
    total = n * m
    if k > total:
        print("Нет")
    elif (k % n == 0 and k // n < m) or (k % m == 0 and k // m < n):
        print("Да")
    else:
        print("Нет")

n = int(input())
m = int(input())
k = int(input())
chocolate(n, m, k)