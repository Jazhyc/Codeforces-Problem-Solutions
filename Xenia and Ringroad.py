n, m = [int(x) for x in input().split()]
p = 1
time = 0
tasks = [int(x) for x in input().split()]

for task in tasks:
    if task < p:
        time += n - p + task
    else:
        time += task - p
    p = task
print(time)