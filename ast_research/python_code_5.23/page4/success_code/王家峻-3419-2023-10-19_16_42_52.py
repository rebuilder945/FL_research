def calDegrees(nums):
       from collections import Counter
       counter=Counter(nums)
       most_common_count=counter.most_common[0]
       d=most_commom_count
       return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

