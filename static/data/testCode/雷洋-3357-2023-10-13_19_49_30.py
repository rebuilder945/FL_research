n = input()
a = input()
v = input()
def Runway(a,v):
    length = v*v/(2*a)
a = float(a)
v = float(v)
print("The acceleration of",n,"is %.2f" % a,"M / s, the take-off speed is %.2f" % v,"M / s, and the shortest take-off runway length is %.2f" % Runway,"M.")
