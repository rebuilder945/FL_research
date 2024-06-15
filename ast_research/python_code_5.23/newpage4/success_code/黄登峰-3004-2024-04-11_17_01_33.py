a=eval(input())
b=[]
for i in a:
    for x in range(2,i):
        if i%x==0:
            b.append(i)
        else:
            continue
print(b)
            
