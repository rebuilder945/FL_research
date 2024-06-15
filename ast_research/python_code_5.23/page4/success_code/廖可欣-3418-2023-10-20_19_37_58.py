def maxsum(y):
    kong = []
    for ai in y:
        y.remove(ai)
        for bi in y:
            c = min(ai,bi)
            kong.append(c)
    return sum(kong)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

