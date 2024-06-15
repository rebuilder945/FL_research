h=eval(input())
N=eval(input())
s=h
for i in range(1,N):
    s+=h
    h=h*0.5
print("%.2f"%s)
