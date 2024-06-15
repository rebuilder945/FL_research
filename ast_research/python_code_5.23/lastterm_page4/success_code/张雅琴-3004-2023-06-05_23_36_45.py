a=eval(input())
b=[]
for i in a: 
    if i==1:
        b.append(i)
    elif i==2:
        b.append(i)   
    else:
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==0:
            b.append(i)
print(b)

