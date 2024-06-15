height=eval(input())
N=eval(input())
h=height
for i in range(N+1):
    h+=h*0.5
print("%.2f"%h)
