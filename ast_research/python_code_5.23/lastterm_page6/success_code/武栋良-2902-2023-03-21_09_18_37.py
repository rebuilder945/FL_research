n = eval(input())
a = 2
b = 1
s = 0
for i in range(0,n):
    c = a/b
    s = s+c
    a,b = a+b,a
print("%.4f"%(s))

