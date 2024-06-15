x=input() or "q"
dic={}
while(x!="q"):
    dic[x]=dic.get(x,0)+1
    x=input() or "q"
ls=[]
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
for i in ls[0]:
    print(i,end="")
