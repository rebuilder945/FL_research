n=list(input().split(','))
m=list(input().split(','))
c1=[]
for i in range(len(n)):
    c=[]
    c.append(n[i])
    c.append(m[i])
    c1.append(c)
for i in range(len(c1)-1):
    a1=c1[i]
    if c1[i][1]>c1[i+1][1]:
        c1[i]=c1[i+1]
        c1[i+1]=a1
    else:
        continue
print(c1)
