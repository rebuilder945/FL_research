l=eval(input())
n,m=eval(input())
l=list(map(int,l))
if l[n]>=l[0] and l[n]<=l[-1]:
    l2=[l[n]]
    s=l2*m
    print(l+s)
else:
    print("error")
