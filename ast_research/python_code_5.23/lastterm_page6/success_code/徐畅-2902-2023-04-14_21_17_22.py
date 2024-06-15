n=eval(input())
a=2
b=1
c=2
for i in range(n-1):
    d=b
    b=a
    a=a+d
    c=(a/b)+c
print("%.4f"%(c))
