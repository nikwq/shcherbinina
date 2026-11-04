# ZADANIE 6
# variant 1
s = input("Введите строку: ")
words = s.split()
c = 0
for word in words:
    if word.lower().startswith('е'):
        c += 1
print(c)

# variant 2
s = input("Введите строку: ")
c = s.count(':')
s = s.replace(':', '%')
print("Количество замен:", c)

# variant 3
s = input("Введите строку: ")
c = s.count('.')
s = s.replace('.', '')
print("Удалено точек:", c)

# variant 4
s = input("Введите строку: ")
c = s.count('а')
s = s.replace('а', 'о')
print("Количество замен:", c)
print("Всего символов в строке:", len(s))

# variant 5
s = input("Введите строку: ")
s = s.lower()
print(s)

# variant 6
s = input("Введите строку: ")
c = s.count('а') + s.count('А')
s = s.replace('а', '').replace('А', '')
print("Удалено букв 'а':", c)

# variant 7
s = input("Введите строку: ")
n = len(s)
half = n // 2
new_s = s[:half].replace('п', '*').replace('П', '*') + s[half:]
print(new_s)

# variant 8
s = input("Введите строку с точкой на конце: ")
words = s.split()
print(len(words))

# variant 9
s = input("Введите текст: ")
search_word = input("Какое слово ищем? ")
words = s.split()
c = 0
for word in words:
    clean_word = word.strip('.,!?;:()"\'')
    if clean_word == search_word:
        c+= 1
print(f"Слово '{search_word}' встретилось {c} раз")

# variant 10
s = input("Введите предложение: ")
print(s.title())

# variant 11
s = input("Введите строку: ")
s = s.replace('!', '.')

max_c = 0
cur_c = 0
for b in s.lower():
    if b == 'н':
        cur_c += 1
        if cur_c > max_c:
            max_c = cur_c
    else:
        cur_c = 0
print(max_c)

# variant 12
s = input("Введите строку: ")
for p in '.,!?;:-()"\'':
    s = s.replace(p, ' ')
for word in s.split():
    if word[-1] == 'я' or word[-1] == 'Я':
        print(word)

# variant 13
s = input("Введите строку со скобками: ")
start = s.find('(')
end = s.find(')')
if start != -1 and end != -1 and start < end:
    print("Символы внутри скобок:", s[start+1:end])
else:
    print("Скобки не найдены или стоят неправильно.")

# variant 14
s = input("Введите строку: ")
for p in '.,!?;:-()"\'':
    s = s.replace(p, ' ')

words = s.split()
print("Слова на 'а':")
for word in words:
    if word.lower().startswith('а'):
        print(word)

print("Слова на 'я':")
for word in words:
    if word.lower().endswith('я'):
        print(word)

# variant 15
s = input("Введите текст: ")
c = s.lower().count('т')
print(c)