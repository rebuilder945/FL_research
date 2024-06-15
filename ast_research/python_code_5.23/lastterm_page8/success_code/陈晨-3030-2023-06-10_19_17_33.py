name=input().split(",")
fen=input().split(",")
dic={}
for x in range(len(name)):
    dic[name[x]]=int(fen[x])
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=False)
print(lst)
