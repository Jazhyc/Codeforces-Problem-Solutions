from sys import stdin
t = int(input())

for _ in range(t):

    n, k = [int(x) for x in stdin.readline().split()]
    a = [int(x) for x in stdin.readline().split()]
    b = [int(x) for x in stdin.readline().split()]

    for __ in range(k):
        amin = min(a)
        bmax = max(b)

        if bmax >= amin:
            a[a.index(amin)] = b.pop(b.index(bmax))
        else:
            break
    
    print(sum(a))