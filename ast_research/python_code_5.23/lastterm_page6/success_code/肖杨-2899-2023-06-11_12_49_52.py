l=input().split()
n=eval(l[0])
m=eval(l[1])
b=list(range(n,m))
if list(b)!=b or len(b)<3 or n<0 or m<0 or b[-1]>9:
    print('illegal input')
else:
    x=[]
    for i in b:
        if i!=0:
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



