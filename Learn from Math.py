n = 10000001
primes = [True] * n
primes[0] = primes[1] = False

i = 2
while i * i <= n:

    if primes[i]:
        for j in range(2, n // i):
            primes[i * j] = False
    i += 1

n = int(input())

for i in range(4, n // 2 + 1):
    if not primes[i] and not primes[n - i]:
        print(i, n - i)
        exit(0)