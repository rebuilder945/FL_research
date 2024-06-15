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
        c=[]
    numbers=[]
    for i in b:
        d=str(i)
        if d[::-1]==d:
            numbers.append(i)
    print(' '.join(str(i) for i in numbers))
elif n<=0 or type(n)==float:
    print('illegal input')
