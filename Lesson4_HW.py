# https://prnt.sc/phn1lm
# Ряд - 1
a = int(input())
b = int(input())

for i in range(a, b + 1):
    print(i)

# Ряд - 2
a = int(input())
b = int(input())

if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

# Ряд - 3
a = int(input())
b = int(input())

for i in range(a, b - 1, -1):
    if i % 2 != 0:
        print(i)

# Сумма десяти чисел
num = 0
for i in range(10):
    num = num + int(input())

print(num)

# Сумма N чисел
n = int(input())

num = 0
for i in range(n):
    num = num + int(input())

print(num)

# https://prnt.sc/phn1dr
# Делаем срезы
s = input()

print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

# Количество слов
print(input().count(" ") + 1)

# Две половинки
s = input()

s1 = s[:(len(s) + 1) // 2]
s = s.replace(s1, "") + s1
print(s)

# Переставить два слова
string = input()

s_list = string.split(" ")
string = s_list[1] + " " + s_list[0]
print(string)
