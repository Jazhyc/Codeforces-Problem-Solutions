for _ in range(int(input())):
    
    nums = [int(x) for x in input().split()]
    n = nums.pop(-1)
    nums.sort()

    n -= 2 * nums[2] - nums[0] - nums[1] # Make candies equal
    if n % 3 == 0 and n >= 0: # Check if remaining candies can be evenly distributed
        print('YES')
    else:
        print('NO')

# c - a, c - b = 2c - a - b
# This isn't communism