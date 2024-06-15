def calDegrees(nums):
    a=[]
    for x in nums:
        d=nums.count(x)
    a.append(d)
    z=max(a)
    return z
    



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

