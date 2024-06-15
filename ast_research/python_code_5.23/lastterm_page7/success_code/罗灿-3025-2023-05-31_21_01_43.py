str=input().split()
dic={}
for i in str:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
ls=[]
for x,y in dic.items():
    ls.append([x,y])
    ls.sort(key=lambda x:x[1],reverse=True)
for a in ls[0:][1]:
    if a==ls[0][1]:
        print('%s %i'%(ls[a][0],ls[a][1]))
