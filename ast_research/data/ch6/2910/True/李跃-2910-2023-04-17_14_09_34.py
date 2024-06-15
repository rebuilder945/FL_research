a=eval(input())
b=eval(input())
d=a
c=0
for n in range(b):
    c=c+a
    a=0.5*a
c=2*c-d
print("%.2f"%(c))
