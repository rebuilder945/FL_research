a=input().split(",")
b=input().split(",")
d=[str(i) for i in b ]
c=[]
for x in range(len(a)):
    c.append(list([a[x],d[x]]))
    c.sort(key=lambda x:x[1])
print(c)
