def maxsum(y):
    sum = 0
    y.sort(revese = False)
    for i in range (len(y)):
        if i%2 == 0:
            sum += y[i]
    return sum
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

