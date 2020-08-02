a = input().lower()
b = input().lower()

test = False
for i, j in zip(a, b):

    if i > j:
        print(1)
        test = True
        break
    
    elif i < j:
        print(-1)
        test = True
        break

if test == False:
    print(0)