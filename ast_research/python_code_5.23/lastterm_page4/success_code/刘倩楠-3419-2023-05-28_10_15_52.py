def calDegrees(nums):
    ls=[]
    for x in nums:
        m=nums.count(x)
        ls.append(m)
        pmax=max(ls)
    return pmax


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

