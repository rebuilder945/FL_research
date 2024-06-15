m=1
t=0
c=[]
while(m):
    x=input()
    if (x!="#"):
        c.append(x)
        t=t+1
    else:
        m=0
print(t,sum(c))
        






