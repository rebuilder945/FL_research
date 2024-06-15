a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if len(b)!=0:
    b.sort()
    
    c = ",".join(map(str,b))
    print(c)
else:
    print('False')     

    
        
    



