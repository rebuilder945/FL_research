def maxsum(nums):
    nums.sort()
    a=nums[1:-1:2]
    sum(a)
    return sum


    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

