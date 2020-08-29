friends = [int(x) for x in input().split()]
friends.sort()
print(friends[1] - friends[0] + friends[2] - friends[1])