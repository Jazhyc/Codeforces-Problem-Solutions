n = int(input())
nums = [int(x) for x in input().split()]
pcount = 0
ccount = 0

for i in nums:

    if i > 0:
        pcount += i
    
    elif i == -1:
        if pcount > 0:
            pcount -= 1
        else:
            ccount += 1

print(ccount)