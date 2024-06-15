x=float(input())
sums=0
if x<20:
    sums=6*(x**2)+1
if 20<=x<40:
    sums=(3*x-60)**0.5
if x>=40:
    sums=100/(x+1)
print("{:.2f}".format(sums))
