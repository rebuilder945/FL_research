h=eval(input())
N=eval(input())
c=h
for i in range(N):
    h=h/2
    c+=h
print("%.2f"%c)
