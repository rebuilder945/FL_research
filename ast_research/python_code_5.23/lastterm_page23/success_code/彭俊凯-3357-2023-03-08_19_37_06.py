from operator import length_hint
from tokenize import Name


Name=input()
a=eval(input())
v=eval(input())
length=v*v/(2*a)
print("The acceleration of%sis%.2fM / s, the take-off speed is%.2fM / s, and the shortest take-off runway length is%.2fM."%(Name,a,v,length))
