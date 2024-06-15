def maxsum(nums):
    nums.sort()
    x=len(nums)-1
    v=0
    for i in range(0,x,2):
        m=nums[i+1]
        v+=m
    return v
        




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

