name=input().split(",")
g=eval(input())
res=[]
for i in range(len(g)):
    b=[name[i],g[i]]
    res.append(b)
print(res)


