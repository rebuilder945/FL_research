a = input().split(" ")
b = input().split(" ")
x = a[eval(b[0])]
del a[eval(b[0])]
a.insert(eval(b[1])-1,x)
print(a)
