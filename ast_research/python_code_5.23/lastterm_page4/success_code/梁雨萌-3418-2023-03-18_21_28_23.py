def maxsum(nums):
    v=0
    nums.sort()
    for i in range(0,len(nums),1):
        u=nums[i]
        v=v+u
    return(v)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

