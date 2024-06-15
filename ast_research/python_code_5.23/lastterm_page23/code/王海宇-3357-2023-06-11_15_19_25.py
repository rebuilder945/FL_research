name=input()
v=eval(input())
a=eval(input())
s=a*a/2/v
final="The acceleration of {n1} is {:0.2f} M/s,the take-off speed is {:0.2f} M / s, and the shortest take-off runway length is {:0.2f} M.".format(n1=name,v,a,s)
print(final)
