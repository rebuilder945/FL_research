a=eval(input())
N=eval(input())
h=a
for x in range(N-1):
    h+=h*0.5*2
print("%.2f"%(h))
