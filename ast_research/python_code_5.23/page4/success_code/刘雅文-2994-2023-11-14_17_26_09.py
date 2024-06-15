

a=list(eval(input()))
n,m=eval(input())
b=[]
if n<=len(a):
    for x in range(m):
        a.append(a[n])
    a=a+b
    print(a)
else:
    print('error')

