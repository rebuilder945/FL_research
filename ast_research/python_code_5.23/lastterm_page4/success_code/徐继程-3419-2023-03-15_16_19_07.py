def calDegrees(list):
    b=list.count(0)
    for nums in range(999):
        a=list.count(nums)
        if a>b:
            b=a
    return b


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

