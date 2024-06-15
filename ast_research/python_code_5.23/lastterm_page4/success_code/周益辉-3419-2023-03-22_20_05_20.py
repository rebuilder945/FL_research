def calDegrees(c):
    max=0
    for i in range(0,10):
        b=c.count(i)
        if b>max:
            max=b
        else:
            pass
    return max


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

