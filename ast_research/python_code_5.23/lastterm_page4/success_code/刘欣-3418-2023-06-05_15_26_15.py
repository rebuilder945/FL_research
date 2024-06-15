def maxsum(nums):
    nums.sort()
    sum1=0
    for i in range(0,len(nums),2):
        sum1+=nums[i]
    return sum1





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

