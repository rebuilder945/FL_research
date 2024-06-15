ls=list(eval(input()))
a,b=eval(input())
c=len(ls)
if a>=c or a<-c:
    print('error')
else:
    d=ls[a]
    for x in range(b):
        ls.append(d)
    print(ls)
   















