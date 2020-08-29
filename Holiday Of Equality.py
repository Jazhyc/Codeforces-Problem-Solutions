n = int(input())

citizens = [int(x) for x in input().split()]
rich = max(citizens)

money = 0

for citizen in citizens:
    money += rich - citizen
print(money)
