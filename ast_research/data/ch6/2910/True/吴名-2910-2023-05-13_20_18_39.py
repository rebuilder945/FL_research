h=eval(input())
N=eval(input())
H=-h
for i in range(N):
    H+=h*((1/2)**i)*2
print("%.2f"%H)
