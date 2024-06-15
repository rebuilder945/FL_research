n = eval(input())
a = 2
b = 1
ls = [2/1]
i = 1
while i < n:
    a = a+b
    b = a-b
    ls.append(a/b)
    i = i + 1
c = sum(ls)
print("%.4f"%c)

