n = int(input())
plevels = set()
X = [int(x) for x in input().split()]
Y = [int(x) for x in input().split()]

for level in X[1:X[0] + 1]:
    plevels.add(level)
for level in Y[1:Y[0] + 1]:
    if level not in plevels:
        plevels.add(level)

if sum(plevels) == (n * (n + 1)) / 2:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")