lst=eval(input())
b=[]
for x in lst:
    if x>2:
        k=0
        for a in range(2,x):
            if x%a==0:
                k+=1
                if k==2:
                    b.append(x)
    elif x==2:
        b.append(x)
    else:
        continue
print(b)
            
