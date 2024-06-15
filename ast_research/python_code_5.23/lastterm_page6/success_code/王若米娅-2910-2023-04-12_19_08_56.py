h=eval(input())
N=eval(input())
c=h
for i in range(1,N):
    h=h*0.5
    c+=h*2
print("%.2f"%c)
