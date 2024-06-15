name=input().split(",")
g=eval(input())
b=[]
res=[]
for i in range(len(g)):
    b.append(name[i])
    b.append(g[i])
    res.append(b)
print(res)


