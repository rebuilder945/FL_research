def calDegrees(nums):
    a=[]
    for n in nums:
        c=nums.count(n)
        a.append(c)
    x=max(a)
    return x


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

