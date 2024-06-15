n=eval(input())
lst=[]
if type(n)!=int or n<=1:
    print('illegal input')
else:
    for i in range(1,n+1):
        m=i
        lst1=[]
        lst2=[]
        for q in str(m):
            lst1.append(q)
        lst1.reverse()
        for p in str(i):
            lst2.append(p)
        if lst1!=lst2:
            continue
        if i<=1:
            continue
        else:
            a=i+2
            for x in range(3,a):
                y=n//x
                if y!=1 and y!=0:
                    continue
        lst.append(i)
for w in lst:
    print(w,end=' ')
