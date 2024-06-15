def maxsum(nums):
    nums1 = nums.sort()
    nums2 = nums[::2]
    h = sum(nums2)
    return h




nums = eval(input())
v = maxsum(nums)#调用自定义函数
print(v)

