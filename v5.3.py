N = int(input('Введите значение N -  '))

a = [0, 1]

for c in range(N+1):
    if N <= 1:
            break
    elif c == 0:
            continue

    a.append(a[c-1]+a[c])

if N > 1:
    a.pop(-1)

print(a)
