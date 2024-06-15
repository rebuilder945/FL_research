def maxsum(x):
    for i,j in x:
        x=i+j
        z=0
        if x>z:
            z=x
        h=0
        if x<h:
            h=x
            return maxsum





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

