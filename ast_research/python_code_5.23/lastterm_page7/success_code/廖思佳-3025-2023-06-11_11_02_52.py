s=input().split()
dic={}
for x in s:
    dic[x] = dic.get(x,0) + 1
ls=list(dic.items())
ls.sort(key=lambda x:x[1],reverse=True)
max=ls[0][1]
ls.sort(key=lambda x:x[0])
for i in ls:
    if ls[i][1]==max:
        print(ls[i][0],ls[i][1])
    else:
        break
