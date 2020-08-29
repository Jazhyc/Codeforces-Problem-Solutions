n, k = [int(x) for x in input().split()]
mins = 240
count = 0
time = 0
for i in range(1, n + 1):
    if time + (5 * i) <= mins - k:
        count += 1
        time += 5 * i
print(count)