def calDegrees(num):
    numcopy = set(num)
    counts = [num.count(i) for i in numcopy]
    return max(counts)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

