a=list(eval(input()))
n,m=input().split(',')
n=eval(n)
m=eval(m)
if n>=-len(a) and n<len(a):
    x=a[n]
    for i in range(m):
        a.append(x)
    print(a)
else:
    print('error')
