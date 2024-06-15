a=input().split(',')
b=input().split(',')
c=[]
for i in range(len(a)):
    d=[a[i],int(b[i])]
    c.append(d)
c.sort(key=lambda x:x[1])
print(c)


