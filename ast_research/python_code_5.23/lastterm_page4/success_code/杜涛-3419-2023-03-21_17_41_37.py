from collections import Counter
def calDgress(a):
    if not a:
        return 0
    count=Counter(a)
    return max(count.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

