g = int(input("Введите число - "))

d = 0
r = 1

while g > 0:
    d = g % 10
    d = d + r
    r = r * r
    g = g // 10

print("Сумма:", d)
print("Произведение:", r)
