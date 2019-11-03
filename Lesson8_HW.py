# Длина отрезка
def distance(a1, b1, a2, b2):
    return ((abs(a1 - a2)) ** 2 + (abs(b1 - b2)) ** 2) ** 0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance(x1, y1, x2, y2))


# Отрицательная степень
def power(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    if n >= 0:
        return result
    else:
        return 1 / result


a = float(input())
n = int(input())

print(power(a, n))


# Большие буквы
def capitalize(string):
    chars = [x for x in string]
    chars[0] = chr(ord(chars[0]) - 32)
    return "".join(chars)


words = input().split()

for word in words:
    print(capitalize(word), end=" ")
