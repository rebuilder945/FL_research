a = input()
b,c=map(int,input().split())
a = a.split()
d = a[b]
a.insert(c,d)
if c >=0:
    e = a.pop(c+1)
else:
    e = a.pop(c)
a.insert(b,e)
if b >=0:
    e = a.pop(b+1)
else:
    e = a.pop(b)
print(a)






