h0=eval(input())
N=eval(input())
h=h0
if N==1:
    h=h0
else:
    for i in range(2,N+1):
        h+=h0/(2**(i-2))
print("%.2f"%(h))

