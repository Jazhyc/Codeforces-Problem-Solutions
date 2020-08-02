colours = [int(x) for x in input().split()]
count = 0
dcolours = []

for colour in colours:

    if colour not in dcolours:
        dcolours.append(colour)
    else:
        count += 1
print(count)