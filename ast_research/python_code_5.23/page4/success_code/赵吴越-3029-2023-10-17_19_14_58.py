def calDegrees(y):
    z=0
    for x in y:
        if y.count(x)>z:
            z=y.count(x);
    return z;

nums =eval(input())
d=calDegrees(nums)
print(d)
