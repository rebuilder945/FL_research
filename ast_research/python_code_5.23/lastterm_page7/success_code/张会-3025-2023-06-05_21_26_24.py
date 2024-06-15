s=input().split()
dic={}
for i in s:
    dic[i]=dic.get(i,0)+1
ls=[]
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
a=ls[0][1]
for i in ls:
    if i[1]==a:
        print(i[0],i[1])
