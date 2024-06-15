def maxsum(nums):
    v=0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>=nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    for i in range(0,len(nums),1):
        u=nums[i]
        v=v+u
    return(v)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

