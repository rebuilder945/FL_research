h0=eval(input())
N=eval(input())
s=0
for i in range(N):
    h=h0*0.5**i
    s+=h*2
s=s-h0
print("%.2f"%(s))
