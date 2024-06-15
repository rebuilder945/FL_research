a = input().split(" ")
w = input().split(" ")
n,m = w[0],w[1]
c,d = max(n,m),min(m,n)
e = a.pop(d)
f = a.pop(c)
a.insert(d,f)
a.insert(c,e)
print(a)

