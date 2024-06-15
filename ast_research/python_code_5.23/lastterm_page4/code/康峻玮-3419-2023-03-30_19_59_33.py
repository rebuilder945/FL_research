def calDegrees(nums):
    x=[]
    for i in nums:
        m=nums.count(i)
        x.append(m)
        y = max(x)
     return y

        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

