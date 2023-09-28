r = int(input('Введите целое положительное число - '))
f = []

if r < 0:
        print('Error')
else:
        while r != 0:
            f.append(r % 10)
            r = r // 10
f.reverse()
print(f)