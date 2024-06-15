a=list(eval(input()))
n,m=eval(input())
if n>len(a):
    print('error')
else:
    b=[a[n+1]]
    b*3
    print(a+b)


