r = int(input())
words = []

for i in range(r):
    words.append(input())

for word in words:

    length = len(word)
    if length <= 10:
        print(word)

    else:
        print(word[0], length - 2, word[-1], sep='')