a=list(eval(input()))
d=len(a)
n,m=eval(input())
if n<(-d) or n>d:
    print('error')
elif 0<=n<=d or (-d)<=n<=-1:
    b=[]
    b.append(a[n])
    a=a+b*m
    print(a)

