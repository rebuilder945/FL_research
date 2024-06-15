from collections import Counter

def calDegrees(nums):
    counter=Counter(nums)
    maxcounter=max(counter.values( ))
    return  maxcounter
   


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

