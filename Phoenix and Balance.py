t = int(input())

for _ in range(t):

    counter = a = b = 0
    coins = []
    n = int(input())

    if n == 2:
        print(2)
        continue

    for i in range(1, n + 1):
        coins.append(2 ** i)
    
    a += coins[-1]
    a += sum(coins[:n //2 - 1])
    b += sum(x for x in coins[n//2 - 1: -1])

    print(abs(a - b))

# A first glance might be a lie