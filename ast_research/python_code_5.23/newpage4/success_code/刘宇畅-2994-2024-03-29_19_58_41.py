a=list(eval(input()))
d=len(a)
n,m=eval(input())
if n<0 or n>d:
    print('error')
elif 0<=n<=d:
    b=[]
    b.append(a[n])
    a=a+b*m
    print(a)

