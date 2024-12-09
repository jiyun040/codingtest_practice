N = int(input()) 
nums = [int(x) for x in input().split()]
nums.sort()
print(int(nums[-1] - nums[0]))