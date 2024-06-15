list=eval(input())
dic={}
sc=''
zq=True
for i in list:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for j in dic.keys():
    if dic[j]==1:
        sc=str(j)+','+sc
        zq=False
sc=sc[:-1]        
if zq:
    print('False')
else:
    print(sc)
