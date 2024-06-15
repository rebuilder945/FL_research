def calDegrees(x):
    du=x.count(x[0])
    for x1 in x:
        if x.count(x1)>du:
            du=x.count(x1)
            return du
        if x.count(x1)==du:
            du=x.count(x[0])
            return du


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

