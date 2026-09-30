import math

# ПРИМЕР 1
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = ((2 * math.cos(x - 2/3)) / (1/2 + math.sin(y)**2)) * (1 + z**2 / (3 - z**2 / 5))
print("s = {0:.6f}".format(s))


# ПРИМЕР 2
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = ((9 + (x - y)**2)**1/3) / (x**2 + y**2 + 2) - math.exp(math.fabs(x - y)) * math.tan(z)**3
print("s = {0:.5f}".format(s))


# ПРИМЕР 3
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = ((1 + math.sin(x + y)**2) / (math.fabs(x - ((2*y) / (1 + x**2 * y**2)))) *
     (x**math.fabs(y)) + math.cos(math.atan(1/z))**2)
print("s = {0:.5f}".format(s))


# ПРИМЕР 4
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = (math.fabs(math.cos(x) - math.cos(y))**(1 + 2 * math.sin(y)**2)) * (1 + z + z**2/2 + z**3/3 + z**4/4)
print("s = {0:.5f}".format(s))


# ПРИМЕР 5
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = math.log(y**(-math.fabs(x))) * (x - y/2) + math.sin(math.atan(z))**2
print("s = {0:.3f}".format(s))


# ПРИМЕР 6
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = math.sqrt(10 * (x**1/3 + x**(y + 2))) * (math.asin(z)**2 - math.fabs(x - y))
print("s = {0:.4f}".format(s))


# ПРИМЕР 7
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = 5 * math.atan(x) - 1/4 * math.acos(x) * (x + 3 * math.fabs(x - y) + x**2) / (math.fabs(x - y) * z + x**2)
print("s = {0:.3f}".format(s))


# ПРИМЕР 8
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = ((math.exp(math.fabs(x - y)) * math.fabs(x - y)**(x + y)) / (math.atan(x) + math.atan(z)) +
     (x**6 + math.log(y)**2)**1/3)
print("s = {0:.4f}".format(s))


# Формула 9
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = math.fabs(x**(y/x) - (y/x)**1/3) + (y - x) * (math.cos(y) - z/(y - x)) / (1 + (y - x)**2)
print("s = {0:.5f}".format(s))


# Формула 10
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = 2**(-x) * math.sqrt(x + (math.fabs(y))**1/4) * (math.exp(x - 1/math.sin(z)))**1/3
print("s = {0:.5f}".format(s))


# Формула 11
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = (y**((math.fabs(x))**1/3) + math.cos(y)**3 * (math.fabs(x - y) * (1 + math.sin(z)**2 / math.sqrt(x + y))) /
     (math.exp(math.fabs(x - y)) + x/2))
print("s = {0:.6f}".format(s))


# Формула 12
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = 2**(y**x) + (3**x)**y - (y * (math.atan(z) - 1/3)) / (math.fabs(x) + 1/(y**2 + 1))
print("s = {0:.5f}".format(s))


# Формула 13
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = ((y + (x - 1)**1/3)**1/4) / (math.fabs(x - y) * (math.sin(z)**2 + math.tan(z)))
print("s = {0:.6f}".format(s))


# Формула 14
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = y**(x + 1) / ((math.fabs(y - 2))**1/3 + 3) + ((x + y/2) / (2 * math.fabs(x + y))) * (x + 1)**(-1/math.sin(z))
print("s = {0:.4f}".format(s))


# Формула 15
x = float(input("Введите x: "))
y = float(input("Введите y: "))
z = float(input("Введите z: "))

s = (((x**(y + 1) + math.exp(y - 1)) / (1 + x * math.fabs(y - math.tan(z)))) * (1 + math.fabs(y - x)) +
     (math.fabs(y - x)**2 / 2) - (math.fabs(y - x)**3 / 3))
print("s = {0:.6f}".format(s))