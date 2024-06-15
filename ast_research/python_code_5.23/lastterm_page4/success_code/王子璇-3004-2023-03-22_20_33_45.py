a=eval(input())
b=[]
for x in a:
    if x==1:
        pass
    else:
        if x==2:
            b.append(2)
        else:
            t=0
            for y in range(2,x):
                if x%y==0:
                    t=t+1
                else:
                    pass
            if t==0:
                b.append(x)
            
       
print(b)
