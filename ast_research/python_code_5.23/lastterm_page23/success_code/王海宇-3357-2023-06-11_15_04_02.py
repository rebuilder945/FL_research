name=input()
v=eval(input())
a=eval(input())
s=a*a/2/v
final="The acceleration of",name,"{0:0.2f}M/s,the take-off speed is {1:0.2f}M / s, and the shortest take-off runway length is {2:0.2f}M.".format(a,v,s)
print(final)
