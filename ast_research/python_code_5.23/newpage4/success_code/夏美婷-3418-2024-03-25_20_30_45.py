def maxsum(nums):
    q=len(nums)
    if q==0 or q==2:
        e=sum(nums)
    else:
        a=max(nums)
        nums.remove(a)
        b=max(nums)
        nums.remove(b)
        c=max(nums)
        nums.remove(c)
        d=max(nums)
        e=b+d
    return e





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

