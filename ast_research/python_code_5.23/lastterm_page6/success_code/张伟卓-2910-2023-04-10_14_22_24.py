a=eval(input())
b=eval(input())
sum=a
for i in range(b-1):
    sum+=a*0.5**i
print("%.2f"%sum)
