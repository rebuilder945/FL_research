def calDegrees(nums):
    ls=[]
    for i in nums:
        m=nums.count(i)
        ls.append(m)
        pmax = max(ls)
return pmax

        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

