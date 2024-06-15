from ast import Del


l=eval(input())
n,m=map(int.input().split(','))
if n<=len(l):
    for x in range(n,m):
        b=l.pop(x)
    print(a)
else:
    print('error')
