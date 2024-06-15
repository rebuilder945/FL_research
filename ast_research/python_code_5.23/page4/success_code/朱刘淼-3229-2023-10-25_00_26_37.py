nums=list(eval(input()))
b=[]
for i in nums:
    a=nums.count(i)
    b.append(a)
c=min(b)
e=[]
if c==1:
    for x in nums:
        d=nums.count(x)
        if d==1:
            e.append(x)
            e.sort()
    print(",".join(map(str,e)))
else:
    print("False")
            
        
        
        
    
