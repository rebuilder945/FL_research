a=input().split(",")
b=input().split(",")
c=[]
for x in range(len(a)):
    c.append(list([a[x],b[x]]))
    c.sort(key=lambda x:x[1])
print(c)
