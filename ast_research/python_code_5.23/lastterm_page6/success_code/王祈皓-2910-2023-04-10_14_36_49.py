h=eval(input())
N=int(input())
s=h
for i in range(1,N):
    s=s+h*2*(0.5)**i
print("%.2f"%s)
