#h=eval(input())
#n=eval(input())
#c=3*h-(h/2**(n-2))
#print("%.2f"%c)
#for循环
h=eval(input())
n=eval(input())
sum=h
for i in range(n-1):
    h=h*0.5
    sum=sum+2*h
print("%.2f"%sum)
