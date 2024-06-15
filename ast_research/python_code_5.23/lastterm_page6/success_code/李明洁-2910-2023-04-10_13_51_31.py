h = int(input())
n = int(input())
sum = h
for x  in range(n-1):
    sum+=h*(0.5)**(x) 
print("%.2f"%(sum))
