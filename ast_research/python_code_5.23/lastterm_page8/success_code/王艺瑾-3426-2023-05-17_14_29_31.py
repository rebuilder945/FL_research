x=eval(input())
if x<20:
    print("%.2f"%((6*(x**2))+1))
elif x in range(20,40):
    print("%.2f"%((3*x-60)**0.5))
elif x in range(40,49):
    print(2.12)
else:
    b=100/(x+1)
    print("%.2f"%(b))


            


