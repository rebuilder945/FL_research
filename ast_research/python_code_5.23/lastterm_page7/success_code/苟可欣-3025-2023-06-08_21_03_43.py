ls=input().split()
ls1=[]
for x in ls:
    k=ls.count(x)
    ls1.append([x,k])
ls2=set(ls1)
ls1=list(ls2)
ls1.sort()
ls1.sort(key=lambda x:x[1],reverse=True)
k1=ls[0][1]
for x in ls1:
    if x[1]==k1:
        print(x[0],x[1])
    else:
        break
