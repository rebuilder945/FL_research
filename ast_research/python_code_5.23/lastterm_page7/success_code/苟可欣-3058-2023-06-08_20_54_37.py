x=input()
ls=[]
while x!='q':
    ls.append(x)
    x=input()
ls2=[]
for x in ls:
    k=ls.count(x)
    ls2.append([x,k])
ls2.sort(key=lambda x:x[1],reverse=True)
print(ls2[0][0],ls2[0][1])
