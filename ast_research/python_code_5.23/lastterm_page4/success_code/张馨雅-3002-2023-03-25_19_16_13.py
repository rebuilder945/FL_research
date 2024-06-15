nums=eval(input(''))
nums1=sum(nums)/len(nums)
if nums1%1>0.001:
    print("%.2f"%nums1)
else:
    print("%d"%nums1)
