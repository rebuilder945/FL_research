def calDegrees(nums):
    a=[]
    for x in nums:
        b=count(a)
        a.append(b)
    z=max(nums)
    return z
    


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

