def calDegrees(x):
    jishu=1
    for x1 in x:
        if x.count(x1)>jishu:
            jishu=x.count(x1)
    return jishu


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

