name=input().split(',')
xuehao=input().split(',')
lsname=list(name)
lsxuehao=list(xuehao)
ls=[]
for x in range(lsname):
    c=lsname[x]+lsxuehao[x]
    ls.append(c)
ls.sort(key=lambda x:x[1])
print(ls)
