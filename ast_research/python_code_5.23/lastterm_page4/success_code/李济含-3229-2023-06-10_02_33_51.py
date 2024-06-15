nums=eval(input())
nums2=[]
for x in nums:
    if x not in nums2:
        nums2.append(x) 
nums2.sort()
if len(nums2)==0:
    print("False")
else:
    x=map(str,nums2)
    x2=",".join(x)
    print(x2)


    


