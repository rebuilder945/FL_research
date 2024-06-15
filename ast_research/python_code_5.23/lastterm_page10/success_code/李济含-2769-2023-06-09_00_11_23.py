def zuobiao(x,lst1):
    for i in range(5):
        for j in range(5):
            if lst1[i][j]==x:
                return [i,j]
def xunzhao(x,y,lst1):
    a=zuobiao(x,lst1)
    b=zuobiao(y,lst1)
    if a[0]!=b[0] and a[1]!=b[1]:
        c=lst1[a[0]][b[1]]+lst1[b[0]][a[1]]
    else:
        c=y+x
    return c
def cunzai(x,lst1):
    jishu1=1
    jishu2=1
    for i in lst1:
        if x[0] in i:
            jishu1=0
        if x[1] in i:
            jishu2=0
    if jishu1==0 and jishu2==0:
        return 0
    else:
        return 1
chuan="abcdefghijklmnopqrstuvwxyz"
yao=input()
mi=input()
lst1=[]
lst2=[]
lst3=[]
for i in yao:
    lst1.append(i)
    if len(lst1)==5:
        lst2.append(lst1)
        lst1=[]
for i in chuan:
    if i not in yao:
        lst1.append(i)
    if len(lst1)==5:
        lst2.append(lst1)
        lst1=[]
lst1=[]
for i in mi:
    lst1.append(i)
    if len(lst1)==2:
        lst3.append(lst1)
        lst1=[]
if len(lst1)!=0:
    lst3.append(lst1)
c=""
for i in lst3:
    if len(i)==1:
        c+=i[0]
    elif i[0]==i[1]:
        c=c+i[0]+i[1]
    elif cunzai(i,lst2):
        c=c+i[0]+i[1]
    else:
        c+=xunzhao(i[0],i[1],lst2)
print(c)



