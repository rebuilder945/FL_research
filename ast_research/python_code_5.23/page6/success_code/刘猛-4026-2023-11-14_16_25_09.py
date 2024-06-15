n = int(input())
a = 2 
b = 1
c = []
for i in range(n):
    c.append(a/b)
    a,b = a+b,a
d = sum(c)
print("%.4f"%d)




