n=list(input())
ls=[]
if len(n)==0:
    print('None')
else:
    for i in n:
        if n.count(i)==1:
            ls.append(i)
    print(ls[0])
