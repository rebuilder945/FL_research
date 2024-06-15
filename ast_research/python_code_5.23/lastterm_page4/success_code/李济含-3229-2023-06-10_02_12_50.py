nums=eval(input())
nums2=[]
for x in nums:
    if x not in nums2:
        nums2.append(x) 
        nums2.sort()
        x=map(str,nums2)
        print(x) 

    else:
        print("False")

    


