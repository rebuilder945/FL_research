n=eval(input())
a=[i for i in range(1,n+1)]
m=int(a.pop(0))
a.insert(n+1,m)
print(a)
