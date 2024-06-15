from itertools import count
def calDegrees(nums):
    ls=[]
    for x in nums:
        c=nums.count(x)
        ls.insert(0,c)
        d=max(ls)
    return d



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

