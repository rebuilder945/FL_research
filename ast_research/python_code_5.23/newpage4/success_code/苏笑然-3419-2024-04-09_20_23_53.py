def calDegrees(nums):
    a=[]
    for x in nums:
        c=nums.count(x)
        a.append(c)
    an=max(a)
    return an


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

