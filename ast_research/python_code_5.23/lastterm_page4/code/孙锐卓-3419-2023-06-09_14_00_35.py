def calDegrees(a)
    for i in a:
        b=a.count(i)
    return max(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

