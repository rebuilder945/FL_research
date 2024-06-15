def maxsum(nums):
    n = len(nums) // 2
    nums.sort()
    b = []
    for i in range(n):
        b.append(nums[2*i])   
    return sum(b)
    return max(b)+min(b)




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

