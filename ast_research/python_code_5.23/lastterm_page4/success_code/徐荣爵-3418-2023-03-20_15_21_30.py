def maxsum(nums):
    nums.sort()
    n = int(0.5 * len(nums))
    l = 0
    for i in range(n) :
        m = 2*i-2
        l = l + int(nums[m])
    return int(l)    




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

