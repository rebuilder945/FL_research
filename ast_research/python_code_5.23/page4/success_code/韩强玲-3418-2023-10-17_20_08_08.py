def maxsum(y):
    sum = 0
    y.sort(reverse = True)
    x = y[::2]
    for i in range(len(x)):
            sum +=x[i]
            return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

