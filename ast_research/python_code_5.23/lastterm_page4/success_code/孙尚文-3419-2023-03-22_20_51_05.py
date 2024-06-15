def calDegrees(nums):
    a=[]
    for x in nums:
        b=nums.count(x)
    a.append(b)
    z=max(a)
    return z
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

