a=str(input())
b=a.split(',')
c=eval(input())
d=[]
for i in range(len(b)):
    x=b[i]
    y=c[i]
    e=[x,y]
    d.append(e)
print(d)
