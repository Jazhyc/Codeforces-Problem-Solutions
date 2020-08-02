n = input()
lucky = ['4', '7']
count = 0

for i in n:
    if i in lucky:
        count += 1

if count in [4, 7]:
    print("YES")
else:
    print("NO")