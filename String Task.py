vowels = ['a', 'e', 'i', 'o', 'u', 'y']
sentence = input()
op =''
for char in sentence:
    if char.lower() not in vowels:
        op += '.'
        op += char.lower()

    elif char.lower() in vowels:
        continue
print(op) 