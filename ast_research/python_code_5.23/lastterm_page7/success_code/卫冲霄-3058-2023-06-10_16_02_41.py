s=input() or "q"
dic={}
ls=[]
while s!="q":
    dic[s]=dic.get(s,0)+1
    s=input() or 'q'
for k,v in dic.items():
    ls.append([k,int(v)])
ls.sort(key=lambda x:x[1],reverse=True)
print(ls[0][0],ls[0][1],end="")



