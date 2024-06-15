a = input()
[b,c] = eval(input())
a = a.split(" ")
d = a[b]
a.insert(c,b)
e = a[c+1]
del a[c+1]
a.insert(b,e)
del a[b+1]
print(a)






