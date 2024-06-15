nums = eval(input())
nums1 = sum(nums)
nums2 = len(nums)
x = nums1 % nums2
if x == 0:
    nums3 = int(nums1/nums2)
    print(nums3)
else:
    nums4 = float(nums1/nums2)
    print("%.2f"%(nums4))
