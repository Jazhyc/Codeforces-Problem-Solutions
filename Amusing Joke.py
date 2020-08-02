n1 = list(input())
n2 = list(input())
n = n1 + n2
n.sort()
a = list(input())
a.sort()

if n == a:
    print("YES")
else:
    print("NO")