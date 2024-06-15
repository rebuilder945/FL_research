def calDegrees(nums):
    x=[]
    for i in nums:
        m=nums.count(i)
        x.append(m)
        pmax = max(x)
     return pmax

        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

