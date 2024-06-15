h=eval(input())
n=eval(input())
sum=h
for x in range(1,n+1):
    h=h*0.5
    sum+=2*h
    
print("%.2f"%sum)
