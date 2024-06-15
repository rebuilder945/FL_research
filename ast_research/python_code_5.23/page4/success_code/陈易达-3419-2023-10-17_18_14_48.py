from collections import Counter
def calDegrees(a):
    counter = Counter(a)
    b = max(counter.values())
    return(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

