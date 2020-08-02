inp = input().split()
n, k = [int(x) for x in inp]
scores = [int(x) for x in input().split()]
kscore = scores[k - 1]
count = 0
for score in scores:
    if score >= kscore and score > 0:
        count += 1
print(count)