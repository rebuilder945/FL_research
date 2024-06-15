a = input()
b,c=map(int,input().split())
a = a.split()
d = a[b]
a.insert(c,d)
e = a.pop(c+1)
a.insert(b,e)
del a[b+1]
print(a)






