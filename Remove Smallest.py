from sys import stdin

t = int(input())

for _ in range(t):

    n = int(input())
    nums = [int(x) for x in stdin.readline().split()]
    nums.sort()

    for i in range(n - 1):
        if nums[i + 1] - nums[i] > 1:
            print('NO')
            break
    else:
        print('YES') 

# NEVER EVER iterate over an iterable and remove elements in it
