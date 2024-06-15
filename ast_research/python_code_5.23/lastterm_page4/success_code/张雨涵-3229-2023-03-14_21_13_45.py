nums = eval(input())
nums1 = []
for i in nums:
    if nums.count(i)==1:
        nums1.append(i)
if nums1:
    nums1.sort()
    print(",".join(str(x) for x in nums1))
else:
    print("False")
