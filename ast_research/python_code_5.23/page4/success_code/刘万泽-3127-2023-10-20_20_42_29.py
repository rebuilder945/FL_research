n=eval(input())
b=[i for i in range(n)]
q=b[0]
b.pop(0)
t=b.copy()
t.insert(-1,q)
print(t)
