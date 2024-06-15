nums=eval(input())
nums2=[]
for x in nums:
    if x not in nums2:
        nums2.append(x) 
        nums2.sort()
        print(nums2) 

    else:
        print("False")

    


