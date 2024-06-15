h=eval(input())
n=eval(input())
sum=h
for x in range(1,n+1):
    sum+=h
    h=h*0.5
print("%.2f"%sum)
