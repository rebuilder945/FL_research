lst=eval(input())
lsts=list(lst)
n,m=eval(input())
a=len(lst)
if n<=m and m<=a:
    b=[]
    for x in range(n,m):
        b.append(lst[x])
    for y in b:
        lsts.remove(y)
    print(lsts)
else:
    print('error')





