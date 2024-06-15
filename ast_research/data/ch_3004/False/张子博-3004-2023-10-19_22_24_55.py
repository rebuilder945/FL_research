t=eval(input())
for x in t:
    if x==1:
        t.remove(x)
        
    elif int(x)==0:
        t.remove(0)
            
    else:
        for i in range(2,x):
            if  x%i==0:
                t.remove(x)
                break
print(t)    
