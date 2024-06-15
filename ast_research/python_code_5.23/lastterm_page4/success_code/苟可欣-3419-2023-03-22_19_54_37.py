def calDegrees(list):
    for x in list:
        a=''.join(list.count(x))
    return max(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

