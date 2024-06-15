def maxsum(nums):
    nums.sort()
    list=[nums[i] for i in range(0,len(nums),2)]
    b=sum(list)
    return(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

