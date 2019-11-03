## Цикл for
# Сумма кубов
s = 0
for i in range(int(input()) + 1):
    s = s + i ** 3
print(s)


# Факториал
n = int(input())
f = 1
for i in range(1, n + 1):
    if n != 1:
        f = f * i
print(f)


# Сумма факториалов
def faktorial(n):
    f = 1
    for i in range(1, n + 1):
        if n != 1:
            f = f * i
    return f


sum = 0
for i in range(1, int(input()) + 1):
    sum += faktorial(i)

print(sum)


# Количество нулей
q = 0
for i in range(int(input())):
    if int(input()) == 0:
        q += 1
print(q)


# Лесенка
result = ""

for i in range(1, int(input()) + 1):
    result += str(i)
    print(result)


# Потерянная карточка
n = int(input())
numbers = 0
s = n
for i in range(1, n):
    numbers += int(input())
    s += i

print(s - numbers)


## Строки
# Первое и последнее вхождения
string = input()
symbol = "f"
q = string.count(symbol)
if q == 1:
    print(string.find(symbol))
elif q >= 2:
    print(string.find(symbol), string.rfind(symbol))


# Второе вхождение
string = input()
symbol = "f"
q = string.count(symbol)  # количество заданных символов в строке
if q == 1:
    print(-1)
elif q >= 2:
    print(string.find(symbol) + 1  # индекс первого вхождения + 1 (компенсация индекса 0)
          + string[string.find(symbol) + 1:].find(symbol))  # получение второго индекса в подстроке
else:
    print(-2)


# Удаление фрагмента
string = input()
symbol = "h"
print(string[:string.find(symbol)] + string[string.rfind(symbol) + 1:])


# Обращение фрагмента
string = input()
symbol = "h"
print(string[:string.find(symbol)] +
      string[string.rfind(symbol):string.find(symbol):-1] +
      string[string.rfind(symbol):])


# Замена подстроки
string = input()
symbol = "1"
subs = "one"
print(string.replace(symbol, subs))


# Удаление символа
string = input()
symbol = "@"
subs=""
print(string.replace(symbol, subs))


# Замена внутри фрагмента
string = input()
symbol = "h"
subs = "H"
s1 = string[:string.find(symbol) + 1]
s2 = string[string.find(symbol) + 1:string.rfind(symbol)]
s3 = string[string.rfind(symbol):]

print(s1 + s2.replace(symbol, subs) + s3)


# Удалить каждый третий символ
string = input()
result = ""

for i in range(len(string)):
    if i % 3 != 0:
        result += string[i]

print(result)
