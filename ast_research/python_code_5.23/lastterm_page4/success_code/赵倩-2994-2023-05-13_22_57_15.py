a=list(eval(input()))
n,m=eval(input())
if n<=len(a)-1:
    b=a[n]
    c=[b]*m
    a.remove(b)
    h=a+c
    print(h)
else:
    print("error")







