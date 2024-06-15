from collections import Counter

def calDegrees(nums):
    counts = Counter(nums)
    return max(counts, key=counts.get)
#在 max(set(nums), key=list.count) 中，list.count 试图对整数对象进行计数，但是 list.count 是一个列表方法，不能直接应用于整数对象。

nums = eval(input())
d = calDegrees(nums)
print(d)