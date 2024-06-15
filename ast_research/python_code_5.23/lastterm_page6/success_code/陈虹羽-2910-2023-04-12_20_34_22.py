h=eval(input())
N=eval(input())
a=h
for i in range(N-1):
    h=h*0.5
    a+=2*h
print("%.2f"%(a))
    
