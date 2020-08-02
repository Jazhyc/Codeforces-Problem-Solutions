word = input()
ucount = lcount = 0

for letter in word:
    if letter.isupper():
        ucount += 1
    else:
        lcount += 1

if lcount >= ucount:
    print(word.lower())
else:
    print(word.upper())