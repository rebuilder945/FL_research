n = eval(input())
a,b,c = 2,1,0
for i in range(n):
    c = c + a/b
    a,b = a+b,a
print("{:.4f}".format(c))

