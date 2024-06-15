a=eval(input())
b=[]
for x in a :
    for y in range(2,x+1) :
        if (x/2)==1 :
            b.append(x)
        elif x%y!=0:            
            b.append(x)
            break
print(b)
