from operator import length_hint
from tokenize import Name


Name=input()
a=eval(input())
v=eval(input())
length=v*v/(2*a)
print("The acceleration of %s is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M."%(Name,a,v,length))
