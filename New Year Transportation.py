n, t = [int(x) for x in input().split()]
cells = [int(x) for x in input().split()]

position = 1
for i in range(0, n):

    if position > t:
        print('NO')
        exit()
    
    elif position == t:
        print('YES')
        exit()
    
    else:
        position += cells[position - 1]