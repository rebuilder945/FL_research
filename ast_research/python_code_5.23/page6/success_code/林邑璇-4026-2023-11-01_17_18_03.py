a=eval(input())
b=0
for i in range(1,1+a):
    c=i*(i-1)/2+2
    d=c/i
    b+=d
print("%.4f"%b)
