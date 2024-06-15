from operator import length_hint
from os import O_CREAT


n = input()
a = input()
v = input()
def Runway(a,v):
    length = v*v/(2*a)
i = float(a)
j = float(v)
k = float(Runway)
print("The acceleration of",n,"is %.2f" % i,"M / s, the take-off speed is %.2f" % j,"M / s, and the shortest take-off runway length is %.2f" % k,"M.")
