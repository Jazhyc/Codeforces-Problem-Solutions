from math import sqrt
# Sieve of Erastosthenes
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
nums = [int(x) for x in input().split()]

for num in nums:
    root = sqrt(num)

    if root % 1 == 0:
        if primes[int(root)]:
            print("YES")
        else: print("NO")
    else: print("NO")