nums=eval(input())
a=max(nums)
b=min(nums)
nums1=nums.copy()
for x in nums:
    if x ==a or x ==b:
        nums1.remove(x)
print(nums1)

