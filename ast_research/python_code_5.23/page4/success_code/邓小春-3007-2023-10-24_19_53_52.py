
l=eval(input())
n,m=map(int,input().split(','))
if n<=len(l):
    for x in range(n,m):
        b=l.pop(x)
    print(l)
else:
    print('error')
