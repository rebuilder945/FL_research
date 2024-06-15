ls=input().split()
ls1=[]
for x in ls:
    k=ls.count(x)
    if ls1.count([x,k])==0:
        ls1.append([x,k])
ls1.sort()
ls1.sort(key=lambda x:x[1],reverse=True)
k1=ls1[0][1]
for x in ls1:
    if x[1]==k1:
        print(x[0],x[1])
    else:
        break
