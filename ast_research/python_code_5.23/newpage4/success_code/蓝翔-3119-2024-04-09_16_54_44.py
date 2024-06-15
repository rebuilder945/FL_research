nums1 = eval(input())
nums2 = str(nums1)
nums3 = []
for i in nums1:
    if i not in nums3:
        nums3.append(i)
print(nums3)
