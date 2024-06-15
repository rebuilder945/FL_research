 from collections import Counter


def calDegrees(r):
    data=Counter(r)
    t=data.most_common
    return t



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

