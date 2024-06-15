a=input().split(",")
b=list(map(int,input().split(",")))
c=[]
for i in range(len(a)):
    k,v=a[i],b[i]
    c.append([k,v])
c.sort(key=lambda x:x[1],reverse=False)
print(c)
