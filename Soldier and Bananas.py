cost, d, n = [int(x) for x in input().split()]

tcost = 0
for i in range(1, n + 1):
    tcost += i * cost

debt = tcost - d

if debt <= 0:
    print('0')
else:
    print(debt)


