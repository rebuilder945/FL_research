def calDegrees(list):
    x=max(set(list),key=list.count())
    return list.count(x)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

