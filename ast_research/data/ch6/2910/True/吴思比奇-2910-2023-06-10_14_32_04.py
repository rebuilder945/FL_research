h=eval(input())
n=int(input())
sum=0
for i in range(1,n+1):
    if i==1:
        sum=sum+h
    else:
        h=h/2
        sum=sum+h*2
      
print("%.2f"%sum)
