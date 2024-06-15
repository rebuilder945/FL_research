a=eval(input())
b=eval(input())
sum=a
for x in range(b-1):
    sum+=a*0.5**x
print("%.2f" %(sum))
