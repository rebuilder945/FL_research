h=eval(input())
n=eval(input())
sum=h
for x in range(1,n+1):
    sum+=n
    n=n*0.5
print("%.2f"%sum)
