a=eval(input())
b=eval(input())
c=0
for i in range(1,b+1):
    c+=a/2**(i-1)
print("%.2f"%c)

