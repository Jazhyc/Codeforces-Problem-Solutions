from fractions import Fraction
n = Fraction(input())

if n % 2 == 0:
    odd = (n / 2) ** 2
    even = (n / 2) * ((n / 2) + 1)
else:
    odd = ((n + 1) / 2) ** 2
    even = ((n - 1) / 2) * (((n - 1) / 2) + 1) 
sum = even - odd
print(int(sum))