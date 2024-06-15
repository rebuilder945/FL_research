name = str(input())
a = eval(input())
v = eval(input())
length = v * v / 2 / a
m = "The acceleration of %s is %d M / s, the take-off speed is %d M / s, and the shortest take-off runway length is %d M."%(name,a,v,length)
print(m)

