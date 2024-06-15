def maxsum(x):
    x.sort(reverse = True)
    sum = 0
    for i in range(len(x)):
        if i % 2 !=0:
            sum = sum+x[i]
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

