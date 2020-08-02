from math import inf
n, l = [int(x) for x in input().split()]
lanterns = [float(x) for x in input().split()]
lanterns.sort()
maxlen = -inf

for i in range(n - 1):
    d = (lanterns[i + 1] - lanterns[i])
    if d > maxlen:
        maxlen = d

if lanterns[0] > maxlen / 2:
    if l - lanterns[-1] > lanterns[0]:
        print(l - lanterns[-1])
    else:
        print(lanterns[0])

elif l - lanterns[-1] > maxlen / 2:
    print(l - lanterns[-1])

else:
    print(maxlen/2)

# Edge cases can be annoying