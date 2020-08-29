m, s = [int(x) for x in input().split()]
minn = maxn = ''

smin = smax = s

def possible(sum, digits):
    return (sum >= 0 and sum <= (9 * digits))

for i in range(m):
    for j in range(10):
        if (possible(smin - j, m - i - 1) and (i > 0 or j > 0 or (m == 1 and j == 0))):
            minn += str(j)
            smin -= j
            break
    else:
        print(-1, -1)
        exit()

for i in range(m):
    for j in range(9, -1, -1):
        if (possible(smax - j, m - i - 1) and (i > 0 or j > 0 or (m == 1 and j == 0))):
            maxn += str(j)
            smax -= j
            break


if int(minn) == 0 and m != 1:
    print(-1, -1)
else:
    print(minn, maxn)

