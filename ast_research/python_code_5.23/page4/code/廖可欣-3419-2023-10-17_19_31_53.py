def calDegrees(test):
    a= 0
    for i in test:
        if a < test.count(i):
            a = test.count(i)
    return(a)
        return max(dic.values())


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

