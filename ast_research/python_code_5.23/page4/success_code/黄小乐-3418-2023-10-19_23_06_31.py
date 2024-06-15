def maxsum(nums):
    nums.sort()
    n = len(nums)
    sum = 0
    for i in range(0,n,2):
        sum = sum +nums[i]
    return(sum)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

