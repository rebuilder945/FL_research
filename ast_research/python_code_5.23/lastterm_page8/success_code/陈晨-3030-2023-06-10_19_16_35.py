name=input().split(",")
fen=input().split(",")
dic={}
for x in range(len(name)):
    dic[name[x]]=fen[x]
lst=[]
for k,v in dic.items():
    lst.append([k,v])
print(lst)
