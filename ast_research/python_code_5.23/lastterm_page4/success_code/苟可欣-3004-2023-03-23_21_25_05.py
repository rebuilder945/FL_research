lst=eval(input())
b=[]
for x in lst:
    if x>1:
        k=0
        for a in range(2,x):
            if x%a!=0:
                k+=1
            else:
                continue
        if k==0:
            b.append(x)
        else:
            continue

            
print(b)


