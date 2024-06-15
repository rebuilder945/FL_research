a=input()
d=[str(n) for n in a.split(',')]
b=eval(input())
c=[]
for x in range(len(d)):
    c.append([d[x],b[x]])
e=c.copy()
for x in range(len(d)-1):
    if c[x][1]>c[x+1][1]:
        c[x],c[x+1]=c[x+1],c[x]
if c[0][1]>c[1][1]:
    c[0],c[1]=c[1],c[0]        
print(c)    
