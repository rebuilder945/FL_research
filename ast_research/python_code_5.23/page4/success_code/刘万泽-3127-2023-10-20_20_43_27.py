n=eval(input())
b=[i for i in range(1,n)]
q=b[0]
b.pop(0)
t=b.copy()
t.insert(-1,q)
print(t)
