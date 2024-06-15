s=input()
dic={}
while (s!="q"):
    dic[s] = dic.get(s,0) + 1
    s=input()
ls=list(dic.items())
ls.sort(key=lambda x:x[1],reverse=True)
print("%s %d"%(ls[0][0],ls[0][1]))
