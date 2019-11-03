# https://prnt.sc/pith4t
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

# https://prnt.sc/pithp3
# Числа Фибоначчи
n = int(input())
i = 1
num1 = 1
num2 = 0
fibo = 1
if n == 0:
    fibo = 0
elif n == 1:
    fibo = 1
else:
    while i < n:
        fibo = num1 + num2
        num2, num1 = num1, fibo
        i += 1

print(fibo)


# Номер числа Фибоначчи
def fibo_number(n):
    if n == 0:
        fibo = 0
    elif n == 1:
        fibo = 1
    else:
        num1 = 1
        num2 = 0
        for i in range(1, n):
            fibo = num1 + num2
            num2, num1 = num1, fibo
            i += 1
    return fibo


num = int(input())
i = 1
while num >= fibo_number(i):
    if num == fibo_number(i):
        print(i)
        break
    i += 1
else:
    print(-1)

# https://prnt.sc/piti07
# Больше предыдущего
string = input()
nums = [int(n) for n in string.split()]

for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        print(nums[i])

# Соседи одного знака
string = input()
nums = [int(n) for n in string.split()]

for i in range(len(nums) - 1):
    if nums[i] * nums[i + 1] > 0:
        print(nums[i], nums[i + 1])
        break
