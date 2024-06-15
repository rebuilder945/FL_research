def calDegrees(nums):
    c=[]
    for i in nums:
       b=nums.count(i)
       c.append(b)
       d=max(c)
    return d
                   
        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

