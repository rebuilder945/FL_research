n=eval(input())
m=[]
lis=[x for x in range(1,n+1)]
for i in range(1,len(lis)+1):
    m.append(lis[i])
m.append(lis[1])
print(m)
