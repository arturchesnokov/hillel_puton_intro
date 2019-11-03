# Дележ яблок
n = int(input("Please input the number of students: "))
k = int(input("Please input the number of apples: "))

print(k // n)
print(k % n)


# Парты
def desks_need(child):
    return child // 2 + child % 2


room1 = int(input("Please input the number of students in room 1: "))
room2 = int(input("Please input the number of students in room 2: "))
room3 = int(input("Please input the number of students in room 3: "))
print("Desks needed to byu: ")
print(desks_need(room1) + desks_need(room2) + desks_need(room3))

# Шнурки
a = int(input("Please input the size of the horizontal distance between holes:"))
b = int(input("Please input the size of the vertical distance between holes: "))
l = int(input("Please input the length of the free tail: "))
N = int(input("Please input the number of the holes of each row: "))
print("Needed length is: ")
print(l * 2 + a * (N * 2 - 1) + b * (N * 2 - 2))

# Минимум из двух чисел
a = int(input("Please input first number: "))
b = int(input("Please input second number: "))
print("Minimal number is: ")
print(a) if a <= b else print(b)

# Минимум из трех чисел
a = int(input("Please input first number: "))
b = int(input("Please input second number: "))
c = int(input("Please input third number: "))
print("Minimal number is: ")
if c >= a <= b:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
