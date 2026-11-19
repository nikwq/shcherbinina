# ZADANIE 9
#var2.1
N = int(input('N: '))
M = int(input('M: '))
B = []
for i in range(N):
    s = []
    for j in range(M):
        s.append(int(input()))
    B.append(s)

for i in range(N):
    imax = 0
    imin = 0
    for j in range(1, M):
        if B[i][j] > B[i][imax]:
            imax = j
        if B[i][j] < B[i][imin]:
            imin = j
    B[i][0], B[i][imax] = B[i][imax], B[i][0]
    if imin == 0:
        imin = imax
    B[i][M-1], B[i][imin] = B[i][imin], B[i][M-1]
for s in B:
    print(*s)

#var2.2
N = int(input('N: '))
A = []
for i in range(N):
    s = []
    for j in range(N):
        s.append(int(input()))
    A.append(s)

for i in range(N):
    A[i][0], A[i][N-1] = A[i][N-1], A[i][0]
for s in A:
    print(*s)

#var2.3
n = int(input('n: '))
m = int(input('m: '))
A = []
for i in range(n):
    s = []
    for j in range(m):
        s.append(float(input()))
    A.append(s)

imax = jmax = 0
for i in range(n):
    for j in range(m):
        if A[i][j] > A[imax][jmax]:
            imax, jmax = i, j

A[0], A[imax] = A[imax], A[0]

for i in range(n):
    A[i][0], A[i][jmax] = A[i][jmax], A[i][0]
for s in A:
    print(*s)

#var2.4
N = int(input('N: '))
A = []
for i in range(N):
    s = []
    for j in range(N):
        s.append(int(input()))
    A.append(s)

for i in range(N):
    for j in range(N):
        if A[i][j] < 0:
            A[i][j] = 0
        elif A[i][j] > 0:
            A[i][j] = 1
print('Нижняя треугольная матрица:')
for i in range(N):
    for j in range(i + 1):
        print(A[i][j], end=' ')
    print()

#var2.5
n = int(input('n: '))
m = int(input('m: '))
A = []
for i in range(n):
    s = []
    for j in range(m):
        s.append(int(input()))
    A.append(s)

for i in range(n):
    imin = 0
    for j in range(1, m):
        if A[i][j] < A[i][imin]:
            imin = j
    val = A[i][imin]
    if val % 2 == 0:
        A[i][imin] = 0
    else:
        A[i][imin] = 1
for s in A:
    print(*s)

#var2.6
N = int(input('N (нечётное): '))
A = []
for i in range(N):
    s = []
    for j in range(N):
        s.append(float(input()))
    A.append(s)

diag = []
for i in range(N):
    diag.append((A[i][i], i, i))
    diag.append((A[i][N-1-i], i, N-1-i))

best = diag[0]
for item in diag:
    if item[0] > best[0]:
        best = item
max_val, imax, jmax = best

c = N // 2
A[imax][jmax], A[c][c] = A[c][c], A[imax][jmax]
for s in A:
    print(*s)

#var2.7
N = int(input('N: '))
A = []
for i in range(N):
    s = []
    for j in range(N):
        s.append(float(input()))
    A.append(s)

diag = []
for i in range(N):
    diag.append(A[i][i])

trace = sum(diag)
print('Диагональ:', diag)
print('След:', trace)

if trace != 0:
    for i in range(N):
        if i % 2 == 0:
            for j in range(N):
                A[i][j] /= trace
for s in A:
    print(*s)

#var2.8
N = int(input('N: '))
A = []
for i in range(N):
    s = []
    for j in range(N):
        s.append(int(input()))
    A.append(s)

T = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        T[j][i] = A[i][j]
for s in T:
    print(*s)

#var2.9
n = int(input('n: '))
A = []
for i in range(n):
    s = []
    for j in range(n):
        s.append(float(input()))
    A.append(s)

imax = jmax = 0
for i in range(n):
    for j in range(n):
        if abs(A[i][j]) > abs(A[imax][jmax]):
            imax, jmax = i, j

B = []
for i in range(n):
    if i == imax:
        continue
    s = []
    for j in range(n):
        if j == jmax:
            continue
        s.append(A[i][j])
    B.append(s)

print('Наибольший по модулю:', A[imax][jmax], 'в позиции', (imax, jmax))
for s in B:
    print(*s)

#var2.10
M = int(input('M: '))
N = int(input('N: '))
D = []
for i in range(M):
    s = []
    for j in range(N):
        s.append(int(input()))
    D.append(s)

k = int(input('k: ')) - 1

idx = []
for j in range(N):
    idx.append(j)

for p in range(N):
    for q in range(N - 1):
        if D[k][idx[q]] > D[k][idx[q + 1]]:
            idx[q], idx[q + 1] = idx[q + 1], idx[q]

T = []
for i in range(M):
    new_s = []
    for j in range(N):
        new_s.append(D[i][idx[j]])
    T.append(new_s)
for s in T:
    print(*s)

#var2.11
M = int(input('M: '))
N = int(input('N: '))
A = []
for i in range(M):
    s = []
    for j in range(N):
        s.append(int(input()))
    A.append(s)

good = -1
min_prod = 0

for j in range(N):
    good_col = 1
    for i in range(M):
        if abs(A[i][j]) > 10:
            good_col = 0
            break
    if good_col == 0:
        continue
    p = 1
    for i in range(M):
        p = p * A[i][j]
    if good == -1 or p < min_prod:
        good = j
        min_prod = p
if good != -1 and good + 1 < N:
    for i in range(M):
        A[i][good], A[i][good + 1] = A[i][good + 1], A[i][good]
for s in A:
    print(*s)

#var2.12
n = int(input('n: '))
m = int(input('m: '))
A = []
for i in range(n):
    s = []
    for j in range(m):
        s.append(float(input()))
    A.append(s)

last = A[n-1]
for i in range(n - 1):
    for j in range(m):
        A[i][j] -= last[j]
for s in A:
    print(*s)

#var2.13
n = int(input('n: '))
m = int(input('m: '))
A = []
for i in range(n):
    s = []
    for j in range(m):
        s.append(int(input()))
    A.append(s)

imax = jmax = imin = jmin = 0
for i in range(n):
    for j in range(m):
        if A[i][j] > A[imax][jmax]:
            imax, jmax = i, j
        if A[i][j] < A[imin][jmin]:
            imin, jmin = i, j

A[imax][jmax], A[imin][jmin] = A[imin][jmin], A[imax][jmax]
for s in A:
    print(*s)

#var2.14
n = int(input('n: '))
M = [[0 for _ in range(n)] for _ in range(n)]

x = 0
y = 0
dx = 0
dy = 1
for num in range(1, n * n + 1):
    M[x][y] = num
    nx = x + dx
    ny = y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= n or M[nx][ny] != 0:
        dx, dy = dy, -dx
        nx = x + dx
        ny = y + dy
    x = nx
    y = ny
for s in M:
    print(*s)

#var2.15
M = int(input('M: '))
N = int(input('N: '))
R = []
for i in range(M):
    st = []
    for j in range(N):
        st.append(int(input()))
    R.append(st)

best = -1
best_sum = 0
for i in range(M):
    all_odd = 1
    for j in range(N):
        if R[i][j] % 2 == 0:
            all_odd = 0
            break
    if all_odd == 0:
        continue
    s = 0
    for j in range(N):
        s = s + abs(R[i][j])
    if best == -1 or s > best_sum:
        best = i
        best_sum = s
if best == -1:
    print('Таких строк нет')
else:
    print('Номер строки:', best)
    print('Сумма:', best_sum)
for st in R:
    print(*st)