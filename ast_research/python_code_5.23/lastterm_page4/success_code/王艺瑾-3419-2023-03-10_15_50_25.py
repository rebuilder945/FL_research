def calDegrees(a):
    a=eval((input))
    x=max(a,key=a.count)
    return x


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

