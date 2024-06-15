ls=[]
while True:
    a=input()
    if a != 'q':
        ls.append(a)
    else:
        break
zifu=[]
for x in ls:
    a=ls.count(x)
    zifu.append([x,a])
zifu.sort(key=lambda x:x[1],reverse=True)
ls=list(zifu[0])
print(ls[0],ls[1])
