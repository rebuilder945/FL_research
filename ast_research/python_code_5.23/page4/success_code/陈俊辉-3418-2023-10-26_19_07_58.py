def maxsum(x):
    for i,j in x:
        c=i+j
        z=0
        if c>z:
            z=c
        h=0
        if c<h:
            h=c
            return h,c





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

