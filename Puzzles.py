from math import inf
n, m = [int(x) for x in input().split()]
puzzles = [int(x) for x in input().split()]
puzzles.sort()
mindiff = inf
for i in range(m - n + 1):
    diff = puzzles[i + n - 1] - puzzles[i]
    if diff < mindiff:
        mindiff = diff
print(mindiff)

# Numbering Systems are wierd