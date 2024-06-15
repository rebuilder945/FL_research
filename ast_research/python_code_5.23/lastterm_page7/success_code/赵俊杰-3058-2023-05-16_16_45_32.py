while True:
    s=input()
    if s=="p":
        break
dic={}
dic[s]=dic.get(s,0)+1
dicList=[]
for k,v in dic.items():
    dicList.append([k,v])
dicList.sort(key=lambda x:x[1],reverse=True)
ls=dicList[0]
print("%d %d"%(ls[0],ls[1]))
