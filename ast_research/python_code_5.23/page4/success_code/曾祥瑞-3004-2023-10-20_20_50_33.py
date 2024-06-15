a=eval(input())
b=[]
for i in range(a):
    for x in range(2,i):
        if i==2:
            b.append(i)
        elif i%x==0:
            break
        else:
            b.append(i)
            break
print(b)
