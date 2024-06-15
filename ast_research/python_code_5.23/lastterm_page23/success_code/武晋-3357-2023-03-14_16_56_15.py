n = input()
def Length(v,a):
    return v*V/(2*a)
v = eval(input())
a = eval(input())
print("The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M." % (n,a,v,Length(v,a)) )
