def calDegrees(a):
    import statistics
    return statistics.mode(a)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

