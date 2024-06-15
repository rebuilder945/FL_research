n=eval(input())
lst1=[]
lst2=[]
lst3=[]
lst4=[]
if n<0 or type(n)!=int:
    print("illegal input")
else:
    for i in range(2,n+1):
        for x in range(2,i):
            if i%x==0:
                break
        else:
            lst1.append(i)
    for q in lst1:
        m=q
        for s in str(m):
            lst2.append(s)
            lst2.reverse()
        for t in str(q):
            lst3.append(t)
        if lst2==lst3:
            lst4.append(q)
for p in lst4:
    print(p,end=' ')

