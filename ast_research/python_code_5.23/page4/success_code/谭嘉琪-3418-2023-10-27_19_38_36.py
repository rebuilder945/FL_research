def maxsum(nums):
    a=max(nums)
    nums.remove(a)
    b=max(nums)
    nums.remove(b)
    c=max(nums)
    nums.remove(c)
    d=max(nums)
    nums.remove(d)
    e=max(nums)
    nums.remove(e)
    f=b+e
    return(f)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

