n = int(input())
nums = [int(x) for x in input().split()]
maxa = mina = nums[0]
count = 0
for i in range(1, n):

    if nums[i] > maxa:
        count += 1
        maxa = nums[i]

    elif nums[i] < mina:
        count += 1
        mina = nums[i]

print(count)