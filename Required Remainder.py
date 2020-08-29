t = int(input())

for i in range(t):

    x, y, n = [int(x) for x in input().split()]
    # k % x = y
    if n - (n % x) + y <= n:
        print(n - (n % x) + y)
    else:
        print(n - (n % x) - x + y)

# Find Nearest number near n. n % x gives distance between n and multiple of x. After that add x
# Modulus is Distance
# Need to go back a step if remainder is too big
# Undershooting, Overshooting