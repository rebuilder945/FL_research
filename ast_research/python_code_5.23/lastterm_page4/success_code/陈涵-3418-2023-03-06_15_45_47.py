def maxsum(nums):
    nums.sort(reverse=True)
    a=nums[0]
    b=nums[1]
    c=nums[2]
    d=nums[3]
    if nums.count(a)>=4:
        e=2*a
    else:
        e=b+d    
    return e




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

