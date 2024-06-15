nums=eval(input())
nums1=[x for x in  nums if nums.count(x)==1]
if nums1:
    print(','.join(map(str,sorted(nums1))))
else:
    print(False)
