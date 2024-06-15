sName = input()
a = eval(input())
v = eval(input())
length = v*v/(2*a)
sText = "The acceleration of %s is % M / s, the take-off speed is % M / s, and the shortest take-off runway length is%.2f"% (sName,a,v,length)
print(sText)

