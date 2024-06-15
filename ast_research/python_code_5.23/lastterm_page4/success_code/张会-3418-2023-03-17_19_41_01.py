def maxsum(nums):
    sum = 0
    nums.sort(reverse = False)
    sum = 0
    for i in nums:
        if i %2 ==0:
            sum += nums(i)
    return sum




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

