a=eval(input())
b=[]
for x in a :
    for y in range(2,x) :
        if (x/2)==1 :
            b.append(x)
        if (x/2)!=1 and x%y!=0:            
            b.append(x)
            break
print(b)
