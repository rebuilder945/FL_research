n = eval(input())
a = 2
b = 1
ls = [2]
for x in range(n-1):
    a = a+b
    b = a-b
    ls.append(a/b)
r = sum(ls)
print("%.4f"%r)
