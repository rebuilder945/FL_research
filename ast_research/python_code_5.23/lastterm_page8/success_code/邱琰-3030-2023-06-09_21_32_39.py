n1=list(input().split())
n2=list(input().split())
ls=[]
for i in range(len(n1)):
    ls.append([n1[i],int(n2[i])])
ls=sorted(key=lambda x:x[1],reverse=False)
print(ls)
