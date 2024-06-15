def maxsum(nums):
    nums.sort()
    lis = []
    for i in range (0,len(nums),2):
        lis.append(nums[i])
    x = sum(lis)
    return x




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

