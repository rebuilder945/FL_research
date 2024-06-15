lst=input().split()
dic={}
for x in lst:
    dic[x]=dic.get(x,0)+1
aftlst=[]
for k,v in dic.items():
    aftlst.append([k,v])
aftlst.sort(key=lambda x:x[1],reverse=True)

biglen = aftlst[0][1]
mlst = []
for x in aftlst:
    if x[1]==biglen:
        mlst.append(x)
mlst.sort(key=lambda x:x[0][0],reverse=True)
for x in mlst:
    print(x[0],x[1])

