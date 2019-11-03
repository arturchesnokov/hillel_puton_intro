## http://prntscr.com/pfxwex
## Високосный год
year = int(input("Please enter year to check it: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("YES")
else:
    print("NO")

## Сколько совпадает чисел
a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

## http://prntscr.com/pfzdzw
## Последняя цифра числа
num = int(input("Please enter a number: "))

print("Last digit of entered number is: " + str(num % 10))

# МКАД
v = int(input())
t = int(input())

print((v * t) % 109)

## Дробная часть
num = float(input())

print(num % 1)

## Первая цифра после точки
num = float(input())

print(int(num * 10 % 10))

## Конец уроков
n = int(input())

time = 9 * 60 + 45 * n
for i in range(1, n):
    if i % 2 != 0:
        time += 5
    else:
        time += 15
print(time // 60, time % 60)


