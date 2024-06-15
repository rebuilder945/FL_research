def maxsum(nums):
    s=list(nums)
    r=sorted(s)
    i=0
    sum=0
    while (i<len(r)):
        sum=sum+r[i]
        i=i+2
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

