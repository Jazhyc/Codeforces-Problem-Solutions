n, k = [int(x) for x in input().split()]
times = [int(x) for x in input().split()]
times.sort()
counter = teams = 0

for person in times:

    if person + k <= 5:
        counter += 1
        if counter % 3 == 0:
            teams += 1
            counter = 0
    else:
        break

print(teams)