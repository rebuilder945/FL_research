a=input().split(",")
b=input().split(",")
c=len(a)

d=[]
for i in range(0,c):
    e=[a[i],int(b[i])]
    d.append(e)
d= sorted(d, key=lambda x: x[1])
print(d)
 


