def maxsum(nums):
    a=nums.sort()
    b=0
    for i in range(0,len(nums),2):
        b+=nums[i]
    return(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

