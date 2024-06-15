a=eval(input())
b=[]
for i in a:    
    if i!=2:
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==0:
            b.append(i)
if 2 in a:
    b.append(2)
print(b)

