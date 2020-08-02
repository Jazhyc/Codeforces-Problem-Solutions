from sys import exit
field = input()

p = '-1'
for player in field:
    if player != p:
        p = player 
        count = 1
    else:
        count += 1
        if count >= 7:
            print("YES")
            exit()
print("NO")