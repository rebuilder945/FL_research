nums=eval(input())
nums2=[]
nums.sort()
for x in nums:
    if nums.count(x)==1:
       nums2.append(x)
    else:
        pass

if len(nums2)==0:
    print("False")
else:
    for x in nums2:
        print(x,end=",")
