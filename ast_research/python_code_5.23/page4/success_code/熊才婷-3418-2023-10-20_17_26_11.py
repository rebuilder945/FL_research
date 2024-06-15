def maxsum(nums):
    ls=nums.sort()
    x=0
    n=len(ls)
    for i in range(0,n,2):
        a=ls[i]
        b=ls[i+1]
        c=max(a,b)
        x+=c
    maxsum=x
    return maxsum
        




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

