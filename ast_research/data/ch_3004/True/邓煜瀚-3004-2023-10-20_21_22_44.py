a=eval(input())
d=[]
for b in a:
    c=0
    for i in range(1,b+1):
        if b%i>-0.1 and b%i<0.1:
            c+=1
        else:
            pass
    if c==2:
        d.append(b)
print(d)



