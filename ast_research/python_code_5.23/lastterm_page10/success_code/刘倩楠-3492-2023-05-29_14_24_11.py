nums=list(input())
ls=[]
for x in nums:
    m=nums.count(x)
    if m>1:
        ls.append(x)    
    else:
        pass
if len(ls)==0:
    print("None")
else:
    print(ls[0])
