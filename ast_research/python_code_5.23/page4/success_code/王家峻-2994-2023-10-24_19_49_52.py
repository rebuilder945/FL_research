n=eval(input())
a,b=eval(input())
if a>len(n):
    print('erro')
else:
    n.extend([n[a]*b])
    print(n)
