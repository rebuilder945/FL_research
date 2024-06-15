x=eval(input())
if x<20:
    d=6*pow(x,2)+1
    print("%.2f"%d)
if x<40 and x>=20:
    d=(3*x-60)**1/2
    print("%.2f"%d)
if x>=40:
    d=100/(x+1)
    print("%.2f"%d)
