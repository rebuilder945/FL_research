nums1=eval(input())
nums2=[]
for i in nums1:
    if nums1.count(i)==1:
        nums2.append(i)
nums2.sort()
if len(nums2)=0:
    print(False)
else:
    str1=",".join(map(str,nums2))
    print(str1)


