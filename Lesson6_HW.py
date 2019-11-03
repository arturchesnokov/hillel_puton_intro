word = "hello".lower()  # на всякий случай
copy = word
try_counter = 5
used_chars = []
mask = "_"

while try_counter > 0 and len(word) != word.count(mask):
    char = input(
        "Please enter a single alphabet character: ").lower()  # в нижний регсистр чтобы большие буквы тоже считались
    if len(char) != 1 or char not in "abcdefghijklmnopqrstuvwxyz":
        print("Wrong symbol!")
        continue
    if char in used_chars:
        print("You already used this one")
    else:
        if char not in word:
            used_chars.append(char)
            try_counter -= 1
            print("No such character in this word")
            print(f"Your attempts: {try_counter}")
        else:
            word = word.replace(char, mask)
            used_chars.append(char)
            print("You are lucky, correct character!")

print("\nCorrect word is:", copy)
if len(word) == word.count(mask):
    print("You are Winner!")
else:
    print("Not today..")
    print("Letters you don't hit:", word)
print("Used:", used_chars)
