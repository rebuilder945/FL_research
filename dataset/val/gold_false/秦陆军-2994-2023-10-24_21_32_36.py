a = list(input().split(','))
a = list(map(int,a))
n,m = eval(input())
c = len(a)
if n>c:
    print('error')
else:
    while len(a)<=c+m-1:
        b=a[n]
        a.append(b)
    print(a)
   


