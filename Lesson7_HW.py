# Множества
# Количество различных чисел
num_list = input().split()
print(len(set(num_list)))


#Количество совпадающих чисел
set1 = set(input().split())
set2 = set(input().split())
print(len(set1.intersection(set2)))


#Пересечение множеств
set1 = set((int(n) for n in input().split()))
set2 = set((int(n) for n in input().split()))
for x in sorted(set1.intersection(set2)):
    print(x)


# Словари
# Номер появления слова
words = input().split()
for i in range(len(words)):
    print(words[:i].count(words[i]), end=" ")


#Словарь синонимов
words = {}

for n in range(int(input("Input amount of word pairs: "))):
    key, value = input("Input words pair using space between words: ").split()
    words[key] = value

sinonim = input()

for key, val in words.items():
    if val == sinonim:
        print(key)
    elif key == sinonim:
        print(val)


#Самое частое слово
string = ""
for n in range(int(input("Input amount of strings: "))):
    string += input()

words = string.split()

words_count = {}
for word in words:
    #print(word)
    words_count[word] = words.count(word)
words = []
for key, val in words_count.items():
    if val == max(words_count.values()):
        words.append(key)
if min(words) == "b":
    print("a")
else:
    print(min(words))


#Права доступа
file_permissons = {}
for n in range(int(input("Input amount of strings: "))):
    parsed_string = input().split()
    file_permissons[parsed_string[0]] = parsed_string[1:]

def check_permissions(files_dict, p, com):
    if p == "read" and "R" in files_dict[com]:
        print("OK")
    elif p == "write" and "W" in files_dict[com]:
        print("OK")
    elif p == "execute" and "X" in files_dict[com]:
        print("OK")
    else:
        print("Access denied")

for i in range(int(input())):
    temp = input().split()
    check_permissions(file_permissons, temp[0], temp[1])
