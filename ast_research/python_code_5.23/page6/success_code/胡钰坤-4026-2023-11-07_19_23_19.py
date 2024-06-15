n = eval(input())
a , b = 1 , 2
s = 2
for i in range(n-1):
    a , b = b , a + b
    s += b/a
print("%.4f"%(s))
