def maxsum(nums):
    nums=sorted(nums)
    a=[]
    for x in range(0,len(nums),2):
        a.append(nums[x])
    b=sum(a)
    return b
        




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

