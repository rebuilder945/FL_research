def calDgreen(nums):
    a=set(nums)
    t=[]
    for i in a:
        s=nums.count(i)
        t.append(s)
    x=max(t)
    return x


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

