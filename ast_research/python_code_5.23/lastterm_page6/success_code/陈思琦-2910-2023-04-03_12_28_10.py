a=eval(input())
b=eval(input())

f=[]
for i in range(1,b):
    c=2*a*(0.5**i)
    f.append(c)
e=sum(f)+a
print("%.2f" %e)

