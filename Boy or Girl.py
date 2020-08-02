user = input()
letters = []
count = 0

for letter in user:
    if letter not in letters:
        letters.append(letter)
        count += 1

if count % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")