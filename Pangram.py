n = int(input())
string = input().lower()
letters = []
count = 0
for letter in string:
    if letter not in letters:
        count += 1
        letters.append(letter)
if count >= 26:
    print("YES")
else:
    print("NO")