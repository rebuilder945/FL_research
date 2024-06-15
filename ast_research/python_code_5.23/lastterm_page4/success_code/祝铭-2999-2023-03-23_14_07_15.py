
def circleinfo(rad):
    pi = 3.14
    r = rad
    return 2*pi*r,pi*r*r


r = eval(input())
c,a=circleinfo(r)
print("%.2f,%.2f"%(c,a))
