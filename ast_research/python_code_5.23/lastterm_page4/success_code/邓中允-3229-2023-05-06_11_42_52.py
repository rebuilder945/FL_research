nums=eval(input())
nums1=[]
for i in nums:
    if nums.count(i)==1:
        nums1.append(i)
nums1.sort()
if len(nums1)==0:
    print(False)
else:
    s=",".join(map(str,nums1))
    print(s)

