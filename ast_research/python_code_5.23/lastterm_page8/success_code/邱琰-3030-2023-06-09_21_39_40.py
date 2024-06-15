n1=list(input().split())
n2=list(input().split())
ls=[]
for i in range(len(n1)):
    ls2=[]
    ls2.append(n1[i])
    ls2.append(int(n2[i]))
    ls.append(ls2)
ls=sorted(ls,key=lambda x:x[1],reverse=False)
print(ls)
