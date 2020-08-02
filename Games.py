n = int(input())
map = {}
away = []
for i in range(n):
    h, a = [int(x) for x in input().split()]
    away.append(a)
    if h in map:
        map[h] += 1
    else:
        map[h] = 1

count = 0
for team in away:
    try:
        count += map[team]
    except KeyError:
        pass
print(count)