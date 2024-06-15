
t=eval(input())
a,b=eval(input())
if a>len(n):
    print('erro')
else:
    def yi(n,c):
        n.extend([n[c]*b])
        return n
    n=yi(t,b)
    print(n)
