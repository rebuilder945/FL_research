def maxsum(nums):
    nums.sort()
    b = nums[::2]
    a = sum(b)
    return(a)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

