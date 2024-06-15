from collections import Counter
print(Counter(eval(input())).most_common(1)[0][1])


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

