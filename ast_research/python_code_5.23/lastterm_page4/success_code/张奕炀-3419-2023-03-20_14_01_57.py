def calDegrees(a):
    b = max(set(a), key=a.count)
    return(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

