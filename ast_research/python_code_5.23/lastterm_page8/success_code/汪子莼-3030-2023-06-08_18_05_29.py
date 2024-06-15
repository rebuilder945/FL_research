name=input().split(',')
xuehao=input().split(',')
lsname=list(name)
lsxuehao=list(xuehao)
ls=[]
for x in range(len(lsname)):
    c=lsname[x]
    d=lsxuehao[x]
    e=c+','+d
    ls.append(list(e))
ls.sort(key=lambda x:x[1])
print(ls)
