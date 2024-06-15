a=1
b=5
c=a
if b==1:
    print(a)
else:
    for i in range(0,b):
        c+=a/2**i
    print("%.2f"%c)

