n = int(input())
a = 1
b = 2
c = 2
d = 3
sbb = (2/1)+(3/2)
for i in range(1,n-1):
    a,b = b,a+b
    c,d = d,c+d
    sb = d/b
    sbb += sb
if n == 1:
    sbb = 2.0000
print("{:.4f}".format(sbb))
