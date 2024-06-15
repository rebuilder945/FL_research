s=input()
dic={}
while (s!="q"):
    dic[s] = dic.get(s,0) + 1
    s=input()
ls=list(dic.items())
ls.sort(key=lambda x:x[1],reverse=True)
max=ls[0][1]
for i in range(1,len(ls)):
    if ls[i][1]==max:
        print(ls[0][1],ls[i][1])
    else:
        break
