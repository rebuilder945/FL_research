def calDegrees(x):
    jishu=0
    for i in x:
        if x.count(i)>jishu:
            jishu=i
    return i        



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

