a=eval(input())
b=[]
for i in a:
    for x in range(2,i):
        if i%x==0:
            break
        elif i==1 or i==0:
            break
    else:
            b.append(i)
print(b)
        
