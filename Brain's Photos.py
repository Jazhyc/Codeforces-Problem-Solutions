m, n = [int(x) for x in input().split()]
colors = ['C', 'M', 'Y']
for _ in range(m):
    cells = input().split()
    for i in cells:
        if i in colors:
            print("#Color")
            exit()
print("#Black&White")
