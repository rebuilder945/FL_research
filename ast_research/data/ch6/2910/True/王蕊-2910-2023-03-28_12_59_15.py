#高度反弹
h=eval(input())
N=eval(input())
s=h
for x in range(N-1):
    s+=h*(0.5)**(x)
print("%.2f"%s)

