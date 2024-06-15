def calDegrees(nums):
    for x in nums:
        everyv=nums.count(x)
    v=list(everyv)
    maxv=max(v)
    return(maxv)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

