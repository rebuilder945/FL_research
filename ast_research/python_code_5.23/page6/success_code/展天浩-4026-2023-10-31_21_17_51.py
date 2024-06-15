n=int(input())
a=1
b=2
c=2
d=3
e=0
while n>n-2:
    e+=(c+d)/(a+b)
if n==1:
    e=2
elif n==2:
    e=3.5
else:
    e=3.5+e
print("%.4f"%(e))
