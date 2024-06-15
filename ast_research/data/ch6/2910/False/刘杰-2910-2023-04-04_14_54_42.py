h=eval(input())
N=eval(input())
L=h
for i in range(1,N+1):
    L+=2*h*0.5**i
print("%.2f"%L)
