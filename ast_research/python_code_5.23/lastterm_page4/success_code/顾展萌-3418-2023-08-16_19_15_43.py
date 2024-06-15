def maxsum(x):
    sum = 0
    x.sort(reverse = True)
    for i in range(len(x)):
        if i %2 == 0:
            sum += x[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

