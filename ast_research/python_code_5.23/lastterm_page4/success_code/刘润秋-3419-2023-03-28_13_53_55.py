def calDegrees(y):
    a=0;
    for x in y:
        if y.count(x)>a:
           a=y.count(x);
    return a;


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

