a=eval(input())
b=eval(input())
d=b-1
f=[]
for i in range(1,d):
    c=2*a*(0.5**i)
    f.append(c)
e=sum(f)+a
print("%.2f" %e)

