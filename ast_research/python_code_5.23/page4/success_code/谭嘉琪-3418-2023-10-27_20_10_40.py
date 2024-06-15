def maxsum(nums):
    a=len(nums)
    b=a/2
    for i in range(b):
        c=max(nums)
        nums.remove(c)
        d=max(nums)
        nums.remove(d)
        e=max(nums)
        nums.remove(e)
        f=max(nums)
        nums.remove(f)
        g=b+f
        return(g)
        





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

