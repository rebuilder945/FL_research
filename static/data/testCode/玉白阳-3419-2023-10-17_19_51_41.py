def calDegrees(y):
    z=0;
    for x in y:
        if y.count(x)>y:
            z=y.count(x);
    return z;


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

