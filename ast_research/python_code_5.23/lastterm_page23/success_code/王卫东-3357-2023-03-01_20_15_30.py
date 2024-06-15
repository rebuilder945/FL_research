sName = input()
a = float(input())
v = float(input())
length = v*v/a*0.5
last = "The acceleration of %s is %.2f M / s,the take-off speed is %.2f M / s,"\
"and the shortest take-off runway length is %.2f M."% (sName,a,v,length)
print(last)
