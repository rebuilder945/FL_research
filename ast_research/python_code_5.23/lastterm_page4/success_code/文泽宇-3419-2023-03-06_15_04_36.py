def calDegrees(SB):
    m=[SB.count(x) for x in set(SB)]
    return max(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

