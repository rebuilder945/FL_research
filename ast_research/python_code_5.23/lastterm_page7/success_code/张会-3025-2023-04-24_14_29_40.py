s=input().split()
m={}
for i in s:
    m[i]=m.get(i,0)+1
ls=[]
for k,v in m.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
ls1=[]
for i in range(len(ls)):
    if ls[i][1]==ls[0][1]:
        ls1.append(ls[i])
ls1.sort(key=lambda x:x[0],reverse=False)
for j in range(len(ls1)):
    print(ls1[j][0],ls1[j][1])
