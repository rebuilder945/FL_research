def calDegrees(list):
    return list.count(max(set(list),key=list.count()))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

