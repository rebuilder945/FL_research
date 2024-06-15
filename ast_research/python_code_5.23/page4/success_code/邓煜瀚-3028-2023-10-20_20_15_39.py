def i(a,b,c):
    s=[]
    for x in range(b):
        e=c*x+a
        s.append(e)
        return s
n,m,l=eval(input())
g=i(n,m,l)
print(g)

