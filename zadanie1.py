# ЗАДАНИЕ 1
print('Курс Основы программирования начался')

# ЗАДАНИЕ 2
ost = (16823 * 12302) % 3092
print('Остаток от деления:', ost)

# ЗАДАНИЕ 3
age = int(input('Возраст: '))
name = input('Имя: ')

if 0 < age < 75:
    if age >= 16 and name != 'Иван':
        print('Поздравляем, вы поступили вo ВГУИТ')
    elif name == 'Иван':
        print('К сожалению, вы не поступили')
    elif age < 16:
        print('Сначала нужно окончить школу!')
        print('Вам осталось учиться в школе', 16 - int(age), 'лет/года')
else:
    print('Вы не можете поступить')

# ЗАДАНИЕ 4
seconds = int(input('Введите количество секунд: '))

days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"{days}:{hours}:{minutes}:{secs}")

# ЗАДАНИЕ 5
a = int(input('Введите число:'))

rez = a + a**2 + a**3 + a**4 + a**5
print("Результат:", rez)

# ЗАДАНИЕ 6
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))

print('x=', y)
print('y=', x)

# ЗАДАНИЕ 7
number = int(input('Введите число: '))

if number % 2 == 0:
    print('Число четное')
else:
    print('Число нечетное')