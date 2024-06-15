def calDegrees(x):
    jishu = x.count(x[0])  # 初始化计数器为第一个元素出现的次数
    for x1 in x:
        if x.count(x1) > jishu:  # 如果当前元素出现的次数大于当前最大值，则更新最大值
            jishu = x.count(x1)
    return jishu


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

