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