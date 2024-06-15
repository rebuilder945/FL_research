n1,n2,n3,n4=input().split(",")
a=float(n1)
b=float(n2)
c=float(n3)
d=float(n4)
m=a+b+c+d*0.7
n=(60-a-b-c)*10/7
if d>=40:
    print("%.2f"%(m))
else:
    print("%.2f"%(d))
print("%.2f"%(n))
