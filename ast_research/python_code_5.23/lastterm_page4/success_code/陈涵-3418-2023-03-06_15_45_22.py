def maxsum(nums):
    nums.sort(reverse=True)
    a=num[0]
    b=num[1]
    c=num[2]
    d=num[3]
    if nums.count(a)>=4:
        e=2*a
    else:
        e=b+d    
    return e




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

