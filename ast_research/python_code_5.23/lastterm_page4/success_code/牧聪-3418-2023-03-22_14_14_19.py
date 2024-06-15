def maxsum(nums):
    n = len(nums) // 2   
    nums.sort() 
    minsum = sum(nums[i] for i in range (0, len(nums), 2)) 
    maxsum = sum(nums[i] for i in range (n, len(nums), 2))  
    return maxsum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

