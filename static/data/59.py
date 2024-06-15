def maxsum(y):
    total_sum = 0
    y.sort(reverse=False)
    #Python 中的 sort() 方法没有 revese 这个关键字参数，正确的参数是 reverse
    for i in range(len(y)):
        if i % 2 == 0:
            total_sum += y[i]
    return total_sum
    #在 maxsum 函数中有两个 return sum，但是第二个 return sum 是无法达到的，因为第一个 return sum 已经结束了函数的执行。

nums = eval(input())
v = maxsum(nums)
print(v)