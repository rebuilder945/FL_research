def maxsum(nums):
    nums.sort()
    c=len(nums)
    a=nums[0]
    m=int(c/2)
    b=nums[m]
    d=a+b
    return d




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

