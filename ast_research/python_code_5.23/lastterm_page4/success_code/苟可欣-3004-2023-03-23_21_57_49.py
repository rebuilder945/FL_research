lst=eval(input())
b=[]
for x in lst:
    if x>2:
        k=0
        for a in range(2,x+1):
            if x%a!=0:
                k+=1
                if k==x-1:
                    b.append(x)
                    break
            else:
                break
    elif x==2:
        b.append(x)
print(b)
            
