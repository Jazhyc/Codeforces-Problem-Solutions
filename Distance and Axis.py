t = int(input())

for _ in range(t):

    n, k = [int(x) for x in input().split()]

    if k > n:
        print(k - n)
    elif k == n:
        print(0)
    else:
        if k <= (n - 2) and (n - k) % 2 == 0:
            print(0)
        else:
            print(1)