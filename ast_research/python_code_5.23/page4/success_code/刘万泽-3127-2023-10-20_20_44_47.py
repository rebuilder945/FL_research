n=eval(input())
b=[i for i in range(1,n+1)]
q=b[0]
b.pop(0)
t=b.copy()
t.append(q)
print(t)
