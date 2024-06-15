a=eval(input())
b=[]
for x in a:
    if x==2:
        b.append(2)
    else:
        for y in range(2,x):
            if x%y==0:
                break
            else:
                b.append(x)
                break
       
print(b)
