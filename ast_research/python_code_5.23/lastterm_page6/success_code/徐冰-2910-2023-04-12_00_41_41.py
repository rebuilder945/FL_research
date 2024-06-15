h=eval(input())
N=eval(input())
ls=[h]
if N == 1:
    print("%.2f"%h)
else:
    for x in range(1,N):
        h1=2*h*0.5**x
        ls.append(h1)
    a=sum(ls)
    print("%.2f"%a)
