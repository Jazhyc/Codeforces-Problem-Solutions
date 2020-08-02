n = int(input())
coins = [int(x) for x in input().split()]
coins.sort(reverse=True)
tmoney = sum(coins)
mymoney = 0

count = 0
for i in range(n):
    count += 1
    mymoney += coins[i]

    if mymoney > tmoney - mymoney:
        break
print(count)
