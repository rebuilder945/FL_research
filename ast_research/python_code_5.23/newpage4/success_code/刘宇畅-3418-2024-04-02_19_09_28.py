def maxsum(nums):
    nums.sort()
    l=len(nums)
    n=l/2
    step=int(l/n)
    c=[]
    for i in range(0,l,step):
        a=nums[i:i+step]
        b=min(a)
        c.append(b)
    sum(c)
    return sum(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

