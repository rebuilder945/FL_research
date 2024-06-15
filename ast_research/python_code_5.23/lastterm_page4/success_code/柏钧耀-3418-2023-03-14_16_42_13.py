def maxsum(nums):
    a=nums
    m=sorted(a)
    b=m[0::2]
    return sum(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

