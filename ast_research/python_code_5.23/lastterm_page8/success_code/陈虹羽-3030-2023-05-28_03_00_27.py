a=input().split(',')
b=input().split(',')
c=[]
d=len(a)
for i in range(d):
    e=[]
    e.append(a[i])
    e.append(int(b[i]))
    c.append(e)
    c.sort(key=lambda x:x[1])
print(c)

