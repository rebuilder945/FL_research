def calDegrees(y):
    z=1;
    for x in y:
        if y.count(x)>z:
            z=y.count(z);
    return max(z);


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

