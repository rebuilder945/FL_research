
x=eval(input())
for i in range(100,x):
    if i>=1000:
        break
    b=str(i)
    c=[]
    d=0
    for f in range(len(b)):
        c.append(b[f])
    for g in range(len(c)):
        d+=int(c[g])**3
    if i==d:
        print(i)
    

