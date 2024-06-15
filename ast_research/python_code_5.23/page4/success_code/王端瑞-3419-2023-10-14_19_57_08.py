def calDegrees(list):
    m = max(set(list),key=list.count)
    return list.count(m)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

