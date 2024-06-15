nums1=eval(input())
a=nums1.count(0)
while a>=1:
    nums1.remove(0)
nums2=[0]*a
nums1=nums1+nums2
print(nums1)

