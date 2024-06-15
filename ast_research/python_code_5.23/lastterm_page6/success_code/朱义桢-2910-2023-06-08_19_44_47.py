h=eval(input())
n=eval(input())
a=[h]
for i in range(1,n):
    b=h*0.5**(i-1)
    print(b)
    a.append(b)
print("%.2f"%sum(a))
