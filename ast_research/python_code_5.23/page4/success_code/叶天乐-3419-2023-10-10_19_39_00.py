from collections import Counter
nums=eval(input())
counter=Counter(nums)
most_common_element=counter.most_common(1)[0][0]
print(most_common_element)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

