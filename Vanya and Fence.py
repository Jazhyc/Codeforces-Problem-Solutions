n, h = [int(x) for x in input().split()]
friends = [int(x) for x in input().split()]

width = 0
for friend in friends:
    if friend > h:
        width += 2
    else:
        width += 1
print(width)