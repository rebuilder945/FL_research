n = eval(input())
a = 1
b = 2
list =[2]
if n == 1:
    s = sum(list)
else:
    for i in range(n-1):
        a = b
        b = b+a
        c = b/a
        list.append(c)
        s = sum(list)
print("%.4f"%s)
