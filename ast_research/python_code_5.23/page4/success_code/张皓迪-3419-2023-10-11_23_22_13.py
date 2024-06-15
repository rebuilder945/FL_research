from itertools import count

def calDegrees(nums):
    ls=[]
    for x in nums:
        ls.insert(nums.count(x))
        d=max(ls)



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

