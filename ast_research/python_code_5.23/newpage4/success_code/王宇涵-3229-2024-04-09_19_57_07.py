nums = eval(input())
nums1 = nums.copy()
for x in nums:
    if not nums.count(x)==1:
     nums1.remove(x)
nums1.sort()
print(nums1)

