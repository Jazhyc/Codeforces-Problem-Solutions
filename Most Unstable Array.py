t = int(input())

for _ in range(t):

    n, m = [int(x) for x in input().split()]

    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(min(2, n - 1) * m)

# Think harder
# Best scenario is is arr = [0,a,0,b,0 .......]
# a + b + ...... = m
# But when placed in the array, the value doubles
# 2a + 2b + 2c..... = 2m