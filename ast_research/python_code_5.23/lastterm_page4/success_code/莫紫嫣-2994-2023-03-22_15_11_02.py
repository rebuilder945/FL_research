a=eval(input())
n,m=eval(input())
a=list(a)
b=[]
if n>len(a)-1:
    print('error')
else:
    for i in range(m):
        b.append(a[n])
    d=a+b
    print(d)
