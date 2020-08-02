n, t = [int(x) for x in input().split()]
q = list(input())

for i in range(t):
    k = False
    for j in range(len(q) - 1):

        if k == True:
            k = False
            continue

        if q[j] == 'B' and q[j + 1] == 'G':
            q[j], q[j + 1] = q[j + 1], q[j]
            k = True

    

print(''.join(q))