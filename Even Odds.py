n, k = [int(x) for x in input().split()]
if n % 2 == 0:
    if k <= n / 2:
        print(int(2 * k - 1))
    else:
        print(int(2 * (k - ((n) / 2))))
else:
    if k <= n + 1 / 2:
        print(int(2 * k - 1))
    else:
        print(int(2 * (k - ((n + 1) / 2))))

# Nth odd number = 2n - 1
# Nth even number = 2n