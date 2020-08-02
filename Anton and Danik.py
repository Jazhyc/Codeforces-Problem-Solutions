n = int(input())
games = input()
acount = dcount = 0

for game in games:
    if game == 'A':
        acount += 1
    else:
        dcount += 1

if acount > dcount:
    print("Anton")
elif dcount > acount:
    print("Danik")
else:
    print("Friendship")