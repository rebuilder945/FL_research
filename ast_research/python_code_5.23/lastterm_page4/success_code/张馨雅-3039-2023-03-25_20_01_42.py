nums=eval(input(''))
m=max(nums)
n=min(nums)
nums1=nums.copy()
for i in nums:
    if i==m or i==n:
        nums1.remove(i)
print(nums1)
