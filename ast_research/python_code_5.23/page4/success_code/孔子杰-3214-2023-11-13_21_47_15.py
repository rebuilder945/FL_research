nums=eval(input())
s=nums.count(0)
while nums.count(0)>=1:
    nums.remove(0)
nums1=[0]*s
nums2=nums+nums1
print(nums2)

