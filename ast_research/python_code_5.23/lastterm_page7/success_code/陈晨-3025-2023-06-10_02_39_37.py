lst=input().split()
dic={}
for x in lst:
    dic[x]=dic.get(x,0)+1
aftlst=[]
for k,v in dic.items():
    aftlst.append([k,v])
aftlst.sort(key=lambda x:x[1],reverse=True)

biglen = aftlst[0][1]

for x in aftlst:
    if x[1]==biglen:
        print(" ".join(str(x)))

