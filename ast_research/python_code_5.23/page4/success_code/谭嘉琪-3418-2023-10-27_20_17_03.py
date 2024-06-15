def maxsum(nums):
    a=len(nums)
    b=a/2
    g=0
    for i in range(b):
        c=max(nums)
        nums.remove(c)
        d=max(nums)
        nums.remove(d)
        g=g+d
    return(g)
        





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

