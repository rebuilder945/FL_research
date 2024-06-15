def calDegrees(x):
    jishu=x.count(x[0])
    for x1 in x:
        if x.count(x1)>jishu:
            jishu=x.count(x1)
    return jishu




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

