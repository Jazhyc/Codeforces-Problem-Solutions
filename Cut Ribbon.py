from sys import setrecursionlimit
lis = [int(x) for x in input().split()]
n, ls = lis[0], lis[1:]
setrecursionlimit(500000)

memoize = dict()

def solve(num):

    if num in memoize:
        return memoize[num]

    if num == 0:
        return 0
    
    ans = float('-inf')

    for l in ls:
        if num >= l:
            ans = max(ans, 1 + solve(num - l))

    memoize[num] = ans
    return ans 

print(solve(n))

# Pypy takes more memory than python