a=eval(input())
b=[]
for i in a:
    if i==2:
        b.append(i)
    if i>2:
        for x in range(2,i):
            if i%x==0:
                break
            else:
                b.append(i)
                break
        b.append(i)
print(b)
