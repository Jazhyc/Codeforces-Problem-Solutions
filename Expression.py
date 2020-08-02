numbers = []
for i in range(3):
    numbers.append(int(input()))
a, b, c = numbers[0], numbers[1], numbers[2]
nums = [0, 0, 0, 0, 0, 0]

nums[0] = a + b + c
nums[1] = a + b * c
nums[2] = a * b + c
nums[3] = a * b * c
nums[4] = a * (b + c)
nums[5] = (a + b) * c

print(max(nums))

