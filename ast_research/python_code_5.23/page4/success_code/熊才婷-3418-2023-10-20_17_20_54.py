def maxsum(nums):
    ls=random.sample(nums)
    x=0
    for i in range(0,len(ls),2):
        a=ls[i]
        b=ls[i+1]
        c=max(a,b)
        x+=c
    maxsum=x
    return maxsum
        




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

