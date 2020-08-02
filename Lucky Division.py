lucky = ['4', '7']
num = input()
l = len(num)
num = int(num)

lnums = 0
for i in range(l, 0, -1):
    lnums += 2 ** i

n = 3 # 4 - 1
for i in range(lnums): # No of lucky numbers possible

    while True: # Gets lucky numbers
        valid = True
        n += 1
        nchr = str(n)

        for chr in nchr:

            if chr not in lucky:
                valid = False
                break
        
        if valid == True:
            break
    
    if num % n == 0:
        print("YES")
        exit()
print("NO")
