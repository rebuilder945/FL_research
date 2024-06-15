a=eval(input())
c=[]
for b in a:
    c=0
    for i in range(1,b+1):
        if b%i==1:
            c+=1
        else:
            pass
    if c==1 or c==2:
        c.append("b")
print(c)
