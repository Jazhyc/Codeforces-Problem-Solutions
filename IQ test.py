n = int(input())
nums = [int(x) for x in input().split()]
evec = 0
oddc = 0
for i in range(n):
    if nums[i] % 2 == 0:
        evec += 1
        evex = i + 1
    else:
        oddc += 1
        oddc = i + 1
if evec == 1:
    print(evex)
else:
    print(oddc)
