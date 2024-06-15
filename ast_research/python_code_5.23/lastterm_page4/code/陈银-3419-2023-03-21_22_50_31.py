def calDegrees(a):
    z = 0
    for x in a:
        if a.count(x)>z:
        z = a.count(x);
    return z;


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

