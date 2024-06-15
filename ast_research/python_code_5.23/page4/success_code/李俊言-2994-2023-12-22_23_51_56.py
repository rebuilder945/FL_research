ls=list(map(int,input().split(',')))
a,b=eval(input())
c=len(ls)
if a>=c or a<-c:
    print('error')
else:
    for x in range(b):
        d=ls[a]
        ls.append(d)
    print(ls)















