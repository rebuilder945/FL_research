a=eval(input())
b=eval(input())
c=0
for i in range(b):
    c+=2*a*0.5**i
print("%.2f"%(c-a))
