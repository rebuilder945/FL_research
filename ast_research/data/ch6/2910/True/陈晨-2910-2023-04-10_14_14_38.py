h=eval(input())
m=eval(input())
n=1
gaodu=0
gaodu+=h
while n!=m:
    n+=1
    h=0.5*h
    gaodu+=(h)*2
print("%.2f"%(gaodu))
