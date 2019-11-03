words = []
file = open("copy.txt")
for line in file:
    words.append(line.rstrip())

letters = "ailm"

# words = ("amma", "amam", "maam", "ramu", "mama", "mila", "tama", "sams", "aamm", "mmaa","ma ma", "mama ", " mama")
mask = "###a"
len_mask = len(mask)

filtered_list = []
temp_list = []
sorted_letters = sorted(letters)

print(sorted(letters))
print("-" * 10)
for w in words:
    print(sorted(w))
    if len(w) == len_mask:
        if sorted_letters == sorted(w):
            filtered_list.append(w)

print("-" * 10)
print("First pass:", filtered_list)

for i in range(len(mask)):
    if mask[i] != "#":
        for w in filtered_list:
            if w[i] == mask[i]:
                temp_list.append(w)
        filtered_list = temp_list.copy()
        temp_list.clear()

print("Result:", filtered_list)
file.close()
