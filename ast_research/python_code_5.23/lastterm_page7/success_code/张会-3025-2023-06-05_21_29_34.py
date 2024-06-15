s=input().split()
dic={}
for i in s:
    dic[i]=dic.get(i,0)+1
ls=[]
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
a=ls[0][1]
ls1=[]
for i in ls:
    if i[1]==a:
        ls1.append(i)
ls1.sort(key=lambda x:x[0],reverse=False)
for x in ls1:
    print(x[0],x[1])
