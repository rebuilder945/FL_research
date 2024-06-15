def calDegrees(a):
    import statistics
    b=statistics.mode(a)
    return a.count(b)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

