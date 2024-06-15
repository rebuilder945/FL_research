ans=input().split(" ")
dics={}
final=[]
for x in ans:
    dics[x]=dics.get(x,0)+1
num=list(dics.values())
maxm=max(num)
for k,v in dics.items():
    if v==maxm:
        final.append([k,v])
final.sort(key=lambda x:x[0])
for i in final:
    print("{} {}".format(i[0],i[1]))
