letters = ['h', 'e', 'l', 'o', 'dummy']
word = input().lower()
newword = ''

pletter = '' # Previous letter
lprev = False # If l was present previously

# Extracts 'hello' if possible
for char in word:

    if char != letters[0]:
        continue

    elif lprev == True and char == 'l':
        newword += char
        lprev = False
        letters.remove(char)

    elif char != pletter:
        newword += char
        pletter = char
        
        if char == 'l':
            lprev = True
        else:
            letters.remove(char)

if newword == 'hello':
    print('YES')
else:
    print('NO')