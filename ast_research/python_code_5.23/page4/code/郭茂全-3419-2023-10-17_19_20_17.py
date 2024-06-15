for collections import Counter
def calDegrees(nums)
     list=Counter(nums)
     d=max(counter.values())
     return d
     


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

