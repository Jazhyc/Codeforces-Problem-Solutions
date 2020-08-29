nums = [int(x) for x in input().split()]
nums.sort()
abc = max(nums)

ab, bc, ac = nums[:3]

a = abc - bc
b = abc - ac
c = abc - ab
print(a, b, c)