a=eval(input())
b=[]
for x in a:
    k=0
    if x==2:
        b.append(x)
    else:
        for y in range(2,x):
            if x%y!=0:
                k+=1
                continue
            else:
                break
        if k==x-2:
            b.append(x)
print(b)
    
