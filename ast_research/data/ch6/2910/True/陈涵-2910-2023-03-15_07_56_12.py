h=eval(input())
n=eval(input())
s=h
for i in range(n-1) :
    h=h/2
    s=s+2*h
print("%.2f"%(s))    
