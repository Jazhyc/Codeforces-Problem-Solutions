n = int(input())

opinions = [x for x in input().split()]

for opinion in opinions:
    if opinion == '1':
        print('HARD')
        exit()
print('EASY')