name=input().split(',')
lsxuehao=eval(input())
lsname=list(name)
ls=[]
for x in range(len(lsname)):
    item=[]
    item.append(lsname[x])
    item.append(lsxuehao[x])
    ls.append(item)
ls.sort(key=lambda x:x[1])
print(ls)
