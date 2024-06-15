def maxsum(nums:list[int])->int:
    nums.sort()
    res=0
    for i in range (0,len(nums),2):
        res +=nums[i]
    return res




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

