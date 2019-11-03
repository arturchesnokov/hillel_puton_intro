n = 4
# n = int(input())
numbers = 0
s = n + 1

for i in range(1, n + 1):
    numbers += int(input())
    s += i

print(s - numbers)
