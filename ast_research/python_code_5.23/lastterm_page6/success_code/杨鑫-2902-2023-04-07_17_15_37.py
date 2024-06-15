n=eval(input())
a=1
b=2
all=0
c=0
for i in range(n):
    all=all+(b)/a
    c=a
    a=b
    b=c+b
print("%.4f"%all)
