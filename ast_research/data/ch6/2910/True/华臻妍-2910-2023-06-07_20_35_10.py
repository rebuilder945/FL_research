h=eval(input())
n=eval(input())
sum=h
for i in range(1,n):
    h=h*0.5
    sum=sum+h*2
print("%.2f"%sum)
     

