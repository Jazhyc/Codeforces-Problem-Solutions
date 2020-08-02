n = int(input())
qs = []
for i in range(n):
    qs.append(input().split())

qcount = 0
for q in qs:
    if q.count('1') >= 2:
        qcount += 1

print(qcount)