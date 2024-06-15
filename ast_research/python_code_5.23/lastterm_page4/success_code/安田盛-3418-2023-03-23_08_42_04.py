def maxsum(nums):
    nums.sort()
    c=[]
    n=[]
    for x in range(0,len(nums),2):
        s=nums[x:x+2]
        n.append(s)
    for x in range(len(n)):
        a=min(n[x])
        for y in range(x+1,len(n)):
            b=min(n[y])
            c.append(a+b)
    return max(c)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

