num=input()
dic={}
while num!="q":
    dic[num]=dic.get(num,0)+1
ls=[]
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
ls1=ls[0]
s=""
for i in ls1:
    s=s+str(i)+""
print(s)
