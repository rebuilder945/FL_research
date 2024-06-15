def maxsum(nums):
    nums.sort()
    n = len(nums) // 2  #确保将长度 n 转换为整数，以便正确进行切片操作。使用整数除法 // 将 len(nums) / 2 转换为整数，确保 n 是一个整数。
    mi = nums[:n]
    ma = nums[n:]
    return min(ma) + min(mi)

nums = eval(input())
v = maxsum(nums)
print(v)