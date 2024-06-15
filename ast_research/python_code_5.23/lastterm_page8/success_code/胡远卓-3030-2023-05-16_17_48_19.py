names=input().split(',')
mark=eval(input())
res=[]
L=len(names)
for i in range(L):
    res.append([names[i],mark[i]])
res.sort(key=lambda x:x[1])
print(res)
