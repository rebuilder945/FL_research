def calDegrees(list):
    return max(set(list),key=list.count(x))


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

