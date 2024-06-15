def calDegrees(a):
    for x in a:
        c=a.count(x) 
    return max(c)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

