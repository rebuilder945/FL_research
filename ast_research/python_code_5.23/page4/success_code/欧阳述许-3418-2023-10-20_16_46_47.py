def maxsum(nums):
    nums.sort()
    b=0
    for i in range(len(nums)):
        if i%2==0:
            b+=nums[i]
    return(b)





nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

