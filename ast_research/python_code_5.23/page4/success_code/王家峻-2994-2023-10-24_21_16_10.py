
t=list(input().split(','))
a,b=eval(input())
if a>len(t):
    print('error')
else:
    for i in range(b):
        t.index(a)
    print(t)
