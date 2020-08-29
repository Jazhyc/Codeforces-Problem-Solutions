k = int(input())

if k % 2 == 0:
    print(k // 2)
    print(('2 ' * (k // 2)).rstrip())
else:
    print(((k - 3) // 2) + 1)
    print(('2 ' * ((k - 3) // 2)) + '3')