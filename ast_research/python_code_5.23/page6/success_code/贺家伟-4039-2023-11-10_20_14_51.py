a=eval(input())
if a<20:
    s=6*a*a+1
    print("%.2f"%(s))
elif a in range(20,40):
    s=(3*a-60)**0.5
    print("%.2f"%(s))
elif a>=40:
    s=100/(a+1)
    print("%.2f"%(s))
else:
    print("2.12")
