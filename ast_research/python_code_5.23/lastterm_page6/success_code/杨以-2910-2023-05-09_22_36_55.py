h=eval(input())
n=eval(input())
if n==1:
    h=h*1
else:
    h=(3-(1/2)**(n-2))*h
print("%.2f"%(float(h)))

