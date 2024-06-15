a=input().split(",")
b=list(map(int,input().split(",")))
c=[]
for i in range(len(a)):
    c.append([a[i],b[i]])
    c.sort(key=lambda x:x[1])
print(c)

