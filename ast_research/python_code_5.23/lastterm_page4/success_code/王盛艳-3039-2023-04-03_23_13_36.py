nums = eval(input())
s1 = max(nums)
s2 = min(nums)
nums1 = nums.copy()
for x in nums:
    if x == s1 or x == s2:
        nums1.remove(x)
print(nums1)
