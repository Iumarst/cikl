g = int(input("Введите число - "))
m = 0

while g > 0:
    if g % 2 == 0:
        m += g % 10
    g //= 10

print(m)