table = input()
cards = input().split()

for card in cards:
    if table[0] in card or table[1] in card:
        print('YES')
        break
else:
    print("NO")