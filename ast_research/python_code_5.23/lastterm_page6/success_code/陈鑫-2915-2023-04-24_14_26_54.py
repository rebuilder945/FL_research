x=eval(input())
for i in range(100,x+1):
    b=str(i)
    c=[]
    d=0
    for i in range(len(b)):
        c.append(b[i])
    for i in range(len(c)):
        d+=int(c[i])**3
