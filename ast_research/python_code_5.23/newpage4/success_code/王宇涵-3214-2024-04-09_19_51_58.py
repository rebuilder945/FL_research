nums = eval(input())
nums1 =nums.copy()
for x in nums:
    if x==0:
     nums1.remove(x)
     nums1.append(0)
print(nums1)

