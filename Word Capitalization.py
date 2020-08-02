word = input()
l = word[0]
new = ''
new += l.upper()
for i in range(1, len(word)):
    new += word[i]
print(new)