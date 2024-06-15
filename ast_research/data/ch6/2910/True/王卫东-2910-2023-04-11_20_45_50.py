a=int(input())
b=int(input())
c=a
for x in range(1,b):
    c = c+2*a*(0.5**int(x))
print("%.2f"%c)    
        
