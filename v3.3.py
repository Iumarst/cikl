b = int(input('Введите число - '))
l = int(input('Введите степень - '))
m = 1

if l > 0:
        for m in range(l+1):
            if m == 0:
                continue

            m*=b
        print(m)