def calDegrees(nums):
    list=[nums]
    d=max(list.count())
    return d


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

