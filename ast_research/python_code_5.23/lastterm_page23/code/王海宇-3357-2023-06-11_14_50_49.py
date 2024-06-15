name=input()
v=eval(input())
a=eval(input())
s=a*a/2/v
final="The acceleration of",name,"is",%.2f,"M/s,the take-off speed is ",%.2f,"M / s, and the shortest take-off runway length is ",%.2f,"M."%(a,v,s)
print(final)
