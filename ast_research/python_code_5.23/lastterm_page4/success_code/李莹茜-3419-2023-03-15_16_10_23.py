def calDegrees(mostls):
    return max(set(mostls),key=mostls.count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

