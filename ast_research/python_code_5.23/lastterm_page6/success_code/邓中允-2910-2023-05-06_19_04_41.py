height=eval(input())
N=eval(input())
h=height
for i in range(N+1):
    h+=h/2
print("%.2f"%h)
