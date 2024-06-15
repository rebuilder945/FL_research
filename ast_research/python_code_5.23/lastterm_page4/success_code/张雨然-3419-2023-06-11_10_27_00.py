def calDegrees(y):
    z=0
    for i in y:
        if y.count(i)>z:
            mmax=y.count(i)
            z=y.count(i)
    return mmax



nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

