def maxsum(nums):
    
    nums.sort(reverse = True)
    c=nums[::2]
    return(sum(c))




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

