a=eval(input())
if a>=40:
    b=100/(a+1)
elif a<20:
    b=6*a*a+1
else:
    b=(3*a-60)**0.5
print("{:.2f}".format(b))

