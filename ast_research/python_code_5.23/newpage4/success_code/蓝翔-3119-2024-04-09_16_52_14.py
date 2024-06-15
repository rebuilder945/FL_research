nums1 = eval(input())
nums2 = []
for i in nums1:
    if i not in nums2:
        nums2.append(i)
print(nums2)
