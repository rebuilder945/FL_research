def calDegrees(nums):
    for x in range(0,len(nums),1):
        everyv=nums.count(x)
        v=list(everyv)
    maxv=max(v)
    return(maxv)


nums = eval(input())
d=calDegrees(nums) #调用自定义函数
print(d)

