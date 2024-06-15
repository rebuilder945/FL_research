nums1 = eval(input())
nums2 = []
for x in nums1:
    if nums1.count(x)==1:
        nums2.append(x)
    if len(nums2)==0:
        print("False")
nums2.sort()
print(nums2)
