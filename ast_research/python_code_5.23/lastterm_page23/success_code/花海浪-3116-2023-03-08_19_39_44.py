a,b=map(eval,input().split(","))
c,d=map(eval,input().split(","))
e=(a-c)**2+(b-d)**2
f=e**(1/2)
print("%.2f"%(f))
