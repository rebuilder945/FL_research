a=eval(input())
b=eval(input())
all=a
for i in range(b-1):
    a=a*0.5
    all=all+2*a
print("%.2f"%all)
    
