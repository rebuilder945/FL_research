def calDegrees(a):
    import statistics
    b=statistics.mode(a)
    c=a.count(b)
    return c



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

