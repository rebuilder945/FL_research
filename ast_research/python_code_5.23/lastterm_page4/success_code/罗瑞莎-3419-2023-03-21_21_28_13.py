def calDegrees(x):
    for i in eval(input()):
        if i not in x:
            x[i] = 1
        else:
            x[i] += 1
    return max(x.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

