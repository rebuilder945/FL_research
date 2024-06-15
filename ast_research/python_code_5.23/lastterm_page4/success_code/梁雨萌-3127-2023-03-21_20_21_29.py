n=eval(input())
m=[]
lis=[x for x in range(1,n+1)]
for i in range(1,n):
    m.append(lis[i])
m.append(1)
print(m)
