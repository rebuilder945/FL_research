def calDegrees(nums):
    x=[]
    for i in nums:
        s=nums.count(i)
        x.append(s)
    z=max(x)
    return z



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

