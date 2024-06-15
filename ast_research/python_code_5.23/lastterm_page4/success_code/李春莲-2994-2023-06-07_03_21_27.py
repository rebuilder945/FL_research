l=eval(input())
n,m=eval(input())
l=list(map(int,l))
if n<=len(l):
    l2=[l[n]]
    s=l2*m
    print(l+s)
else:
    print("error")
