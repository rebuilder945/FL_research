n=eval(input())
if n>0 and type(n)==int:
    b=[]
    c=[]
    for i in range(n+1):
        for x in range(1,i):
            if i%x==0:
                c.append(x)
        if len(c)==1:
                b.append(i)
    for i in b:
        c=str(i)
        if c[::-1]!=c:
            b.remove(i)
    print(''.join(str(i) for i in b))
elif n<=0 or type(n)==float:
    print('illegal input')
