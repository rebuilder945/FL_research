n,m,l=eval(input())
slist=[]
for i in range(m):
    if i==0:
        n=n
    else:
        n+=l
    slist.append(n)
print(slist)



