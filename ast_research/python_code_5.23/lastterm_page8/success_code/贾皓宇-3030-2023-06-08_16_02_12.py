a=list(input().split(','))
b=list(input().split(','))
c=[]
for i in range(len(a)):
    d=[a[i],b[i]]
    d[1]=int(d[1])
    c.append(d)
c.sort()
print(c)
