a=eval(input())
b=eval(input())
s=a
x=1
for x in range(1,b):
    a=0.5*a
    s+=2*a
    x+=1
print("%.2f"%s)    
