from collections import Counter
def calDegrees(nums):
     list=Counter(nums)
     b=max(list.values())
     return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

