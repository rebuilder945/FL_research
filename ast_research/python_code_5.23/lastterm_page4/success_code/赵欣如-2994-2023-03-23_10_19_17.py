ls=list(eval(input()))
n,m=eval(input())
if n not in range(0,len(ls)-1):
    print("error")
else:
    b=str(ls[n])*m
    c=",".join(b)
    a=list(eval(c))
    print(ls+a)


