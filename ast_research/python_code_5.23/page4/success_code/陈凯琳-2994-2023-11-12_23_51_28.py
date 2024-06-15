a=list(eval(input()))
n,m=eval(input())
if n<-(len(a))or n>(len(a)-1):
    print('error')
else:
    b=a[n]
    for i in range(m):
        a.append(b)
    print(a)
