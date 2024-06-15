a=list(eval(input()))
n,m=eval(input())
if n>len(a):
    print("error")
else:
    b=[a[n]]*m
    a=a+b
    print(a)


