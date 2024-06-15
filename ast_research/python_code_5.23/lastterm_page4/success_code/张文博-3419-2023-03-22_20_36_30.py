def calDegrees(list):
    return max(key=list.count)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

