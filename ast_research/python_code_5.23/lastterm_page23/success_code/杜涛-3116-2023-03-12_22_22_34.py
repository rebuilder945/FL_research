a,b=map(eval,input().split(","))
c,d=map(eval,input().split(","))
f=(a-c)**2+(b-d)**2
L=f**(1/2)
print("%.2f"%(L))
