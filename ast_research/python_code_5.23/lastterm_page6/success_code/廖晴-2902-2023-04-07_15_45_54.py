a=2/1
n=eval(input())
s=a
for i in range(1,n):
    b=1/a
    a=b+1
    s+=a
print("%.4f"%s)
