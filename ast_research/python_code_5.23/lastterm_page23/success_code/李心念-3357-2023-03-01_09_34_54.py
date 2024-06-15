sname = input()
a = eval(input())
v = eval(input())
v2 = v*v
L = v2/(2*a)

print("The acceleration of",sname,"is %.2f M / s, the take-off speed is %.2f M / s, and the shortest take-off runway length is %.2f M."%(a,v,L))
