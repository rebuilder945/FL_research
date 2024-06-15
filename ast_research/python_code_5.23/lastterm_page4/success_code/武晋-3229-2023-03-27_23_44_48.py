nums1 = eval(input())
nums2 = eval(input())
nums3 = []
for x in nums1:
    if x not in nums2:
        if x not in nums3:
            nums3.append(x);
for x in nums2:
    if x not in nums1:
        if x not in nums3:
            nums3.append(x)
nums3.sort(reverse = False)

print(nums3)
