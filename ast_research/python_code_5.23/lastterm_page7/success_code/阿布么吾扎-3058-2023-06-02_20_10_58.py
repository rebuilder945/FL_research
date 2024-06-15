a=input()
ls1=[]
while a!='q':
    ls1.append(a)
    a=input()
dic={}
for x in ls1:
    dic[x]=dic.get(x,0)+1
ls=list(dic.items())
ls.sort(key=lambda x:x[1],reverse=True)
print("%s %s"%(ls[0][0],ls[0][1]))


