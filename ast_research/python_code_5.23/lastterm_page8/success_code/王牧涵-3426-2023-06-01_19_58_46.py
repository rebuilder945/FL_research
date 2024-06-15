x=float(input())
if x<20:
    sum=6*x*x+1
elif x>=20 and x<40:
    a=3*x-60
    sum=a*0.5
elif x>=40:
    sum=100/(x+1)
print(float(sum))
