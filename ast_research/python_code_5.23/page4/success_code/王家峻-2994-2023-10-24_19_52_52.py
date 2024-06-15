n=eval(input())
a,b=eval(input())
if a>len(n):
    print('erro')
else:
    n.extend([n[a]*b])
    n=n(n,2)
    print(n)
