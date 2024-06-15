n=eval(input())
a=1
b=2
k=0
for i in range (n):
    k+=b/a
    b+=a
    a=b-a
print("%.4f"%k)
