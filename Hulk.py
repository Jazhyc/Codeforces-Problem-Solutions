n = int(input())

words = ['I hate it', 'I hate that', 'I love it', 'I love that']
word = ''
for i in range(n):
    if i % 2 == 0:
        if i != n - 1:
            word += words[1] + ' '
        else:
            word += words[0]
    else:
        if i != n - 1:
            word += words[3] + ' '
        else:
            word += words[2]
print(word)