nums1=eval(input())
avg=sum(nums1)/len(nums1)
if sum(nums1)%len(nums1)==0:
    print(int(avg))
else:
    print("%.2f"%(avg))
