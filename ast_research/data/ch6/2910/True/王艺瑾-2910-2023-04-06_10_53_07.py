a=eval(input())
b=eval(input())
c=1
l=a
while c<b:
    l=l+a
    a=a*0.5
    c+=1
print("%.2f"%(l))

