h=eval(input())
N=eval(input())
s=0
while N>1:
    s+=h*1.5
    h*=0.5
    N-=1
s=s+h
print("%.2f"%s)
