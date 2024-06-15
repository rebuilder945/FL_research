a=input().split(',')
b=input().split(',')
b=list(map(eval,b))
c=[]
for x in range(len(a)):
    d=[a[x],b[x]]
    c.append(d)
c.sort(key=lambda x:x[1])
print(c)
