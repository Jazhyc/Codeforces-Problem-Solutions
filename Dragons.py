from sys import stdin
s, n = [int(x) for x in input().split()]
pairs = []
for i in range(n):
    d, p = [int(x) for x in stdin.readline().split()]
    pairs.append([d, p])

map = sorted(pairs, key = lambda x: x[0])
for level in map:
    if level[0] < s:
        s += level[1]
    else:
        print("NO")
        exit()
print("YES")

# Be careful with dictionaries, don't assume all keys are unique for assignment