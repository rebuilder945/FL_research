from collections import Counter
def calDegrees(lst):
    counter=Counter(lst)
    max_count=max(counter.values())
    max_elements=[k for k,v in counter.items() if v==max_count]
    return max_elements
nums = eval(input())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

