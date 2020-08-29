import sys
sys.setrecursionlimit(50000)
n = int(input())
nums = [int(x) for x in input().split()]
largest = max(nums)

arr = [0] * 100001
dp = [None] * 100001
for i in nums:
    arr[i] += 1

dp[0] = 0
dp[1] = 1 * arr[1]

for i in range(2, 100001):
    dp[i] = max(dp[i - 1], i * arr[i] + dp[i - 2])

print(max(dp))