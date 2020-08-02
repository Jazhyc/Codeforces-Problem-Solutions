n = int(input()) 
teams = [int(x) for x in input().split()]
count1 = count2 = count3 = count4 = 0

for i in teams:
    if i == 1:
        count1 += 1
    elif i == 2:
        count2 += 1
    elif i == 3:
        count3 += 1
    else:
        count4 += 1

count = count4
count += count2 // 2
count2 %= 2

if count1 <= count3:
    count += count1
    count += count2
    count += count3 - count1
else:
    count += count3
    count1 -= count3
    count += count1 // 4
    count1 %= 4

    rem = count1 + count2 * 2
    if rem > 0:
        if rem <=4:
            count += 1
        else:
            count += 2  
    
print(count)