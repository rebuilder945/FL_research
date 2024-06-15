s=eval(input())
dic={}
for i in s:
    for j in i:
        dic[j]=dic.get(j,0)+1
ls=[]
for k,v in dic.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[0],reverse=False)
for x in ls:
    s1=[str(y) for y in x]
    m=",".join(s1)
    print(m)
