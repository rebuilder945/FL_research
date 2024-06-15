def maxsum(nums):
    nums.sort()
    A = len(nums)
    a = 0
    for i in range(0,A,2):
        b = nums[i]
        a +=b
    return a




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

