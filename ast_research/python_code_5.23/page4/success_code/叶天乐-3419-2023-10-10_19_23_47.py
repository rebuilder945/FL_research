from collections import Counter

nums=input([])
counter=Counter(nums)
most_common=counter.most_common(1)
print(most_common[0][0])


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

