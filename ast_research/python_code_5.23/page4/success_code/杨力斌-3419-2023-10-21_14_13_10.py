def calDegress(lst):
    lstr = [lst.count(x) for x in lst ]
    return max(lstr)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

