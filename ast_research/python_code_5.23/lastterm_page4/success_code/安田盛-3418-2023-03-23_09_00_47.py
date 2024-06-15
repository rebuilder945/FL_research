def maxsum(nums):
    nums.sort()
    c=[]
    n=[]
    b=0
    for x in range(0,len(nums),2):
        s=nums[x:x+2]
        n.append(s)
    for x in range(len(n)):
        a=min(n[x])
        b=b+a
    return b 




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

