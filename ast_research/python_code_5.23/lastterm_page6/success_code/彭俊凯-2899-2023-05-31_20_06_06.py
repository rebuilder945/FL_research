n,m=eval(input())
b=list(range(n,m))
if list(b)!=b or len(b)<3:
    print('illegal input')
else:
    x=[]
    for i in b:
        c=str(i)
        h=i
        for i in b:
            if str(i)!=c:
                t=c+str(i)
                p=i
                for i in b:
                    if str(i)!=str(h) and str(i)!=str(p):
                        o=t+str(i)
                        x.append(o)
    print(' '.join(x))


