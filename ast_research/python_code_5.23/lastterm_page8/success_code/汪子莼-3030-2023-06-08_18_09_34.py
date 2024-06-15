name=input().split(',')
xuehao=input().split(',')
lsname=list(name)
lsxuehao=list(xuehao)
ls=[]
for x in range(len(lsname)):
    item=[]
    item.append(lsname[x])
    item.append(lsxuehao[x])
    ls.append(item)
ls.sort(key=lambda x:x[1])
print(ls)
