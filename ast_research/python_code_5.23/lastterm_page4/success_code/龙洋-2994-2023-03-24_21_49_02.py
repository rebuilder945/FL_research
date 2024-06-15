x=eval(input())
q=list(x)
n,m=eval(input())
o=len(x)
p=-o
if p>n or n>o-1:
    print('error')
else:
    y=q[n]
    for j in range(m):
        q.append(y)
    print(q)
