s=input().split()
m={}
for i in s:
    m[i]=m.get(i,0)+1
ls=[]
for k,v in m.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(len(ls)):
    if ls[i][1]==ls[0][1]:
        print(ls[i][0],ls[i][1])
