a = input().split(" ")
[n,m] = eval(input().split(" "))
c,d = max(n,m),min(m,n)
e = a.pop(d)
f = a.pop(c)
a.insert(f,d)
a.insert(e,c)
print(a)

