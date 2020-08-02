words = input()
d = set()
pwords = words[1 : len(words) - 1].split(', ')
for word in pwords:
    d.add(word)
if d != {''}:
    print(len(d))
else:
    print(0)