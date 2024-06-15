from collections import Counter
def  calDegrees(t):
    p=Counter(t).most_common(1)[0][1]
    return p


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

