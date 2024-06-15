
t=list(input().split(','))
a,b=eval(input())
if a>len(t):
    print('error')
else:
    c=t[a]
    for i in range(b):
         s=t.append(c)
    print(s)
