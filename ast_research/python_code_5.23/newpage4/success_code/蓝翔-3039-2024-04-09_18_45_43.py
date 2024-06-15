nums1 = eval(input())
i = max(nums1)
j = min(nums1)
while i in nums1:
    nums1.remove(i)
while j in nums1:
    nums1.remove(j)
print(nums1)
