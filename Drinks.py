from statistics import mean
n = int(input())

drinks = [int(x) for x in input().split()]
print(mean(drinks))